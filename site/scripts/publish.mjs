// One command for a lesson change made in Drive: two-way sync -> build -> commit. Pushes only with --push.
// Usage: npm run publish -- "message"        (commit locally)
//        npm run publish -- "message" --push (commit and push the current branch)
import { spawnSync } from 'node:child_process';
import { ROOT } from './lessons.mjs';

const args = process.argv.slice(2);
const push = args.includes('--push');
const message = args.filter((a) => a !== '--push').join(' ').trim() || `Sync lessons from Drive ${new Date().toISOString().slice(0, 10)}`;

function run(cmd, cmdArgs, cwd = ROOT) {
	const r = spawnSync(cmd, cmdArgs, { cwd, stdio: 'inherit' });
	if (r.status !== 0) {
		console.error(`\npublish stopped: "${cmd} ${cmdArgs.join(' ')}" failed. Nothing was committed.`);
		process.exit(r.status ?? 1);
	}
}

const site = `${ROOT}/site`;
run('node', ['scripts/sync.mjs'], site);
run('npm', ['run', 'build'], site);

run('git', ['add', 'lessons', 'site/scripts', 'site/src', 'site/astro.config.mjs', 'site/package.json', 'site/package-lock.json', '.gitignore']);
const staged = spawnSync('git', ['diff', '--cached', '--quiet'], { cwd: ROOT });
if (staged.status === 0) {
	console.log('publish: build passed, no changes to commit.');
	process.exit(0);
}
run('git', ['commit', '-q', '-m', message]);
console.log(`publish: committed "${message}"`);

if (push) {
	run('git', ['push', '-u', 'origin', 'HEAD']);
	console.log('publish: pushed. The site deploys when this lands on main.');
} else {
	console.log('publish: not pushed. Run again with --push, or push by hand.');
}
