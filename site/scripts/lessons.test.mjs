// node --test site/scripts
import assert from 'node:assert/strict';
import test from 'node:test';
import { parseMentees, youtubeEmbed } from './lessons.mjs';

test('youtubeEmbed', () => {
	const want = 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ';
	for (const u of ['https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=10s', 'https://youtu.be/dQw4w9WgXcQ?si=x', 'https://www.youtube.com/live/dQw4w9WgXcQ'])
		assert.equal(youtubeEmbed(u), want);
	assert.equal(youtubeEmbed('https://drive.google.com/file/d/abc/view'), null);
	assert.equal(youtubeEmbed(''), null);
});

test('parseMentees keeps only http(s) links and gives each mentee its own slug', () => {
	assert.deepEqual(parseMentees('- [Nguyễn Đức](https://a.github.io/x/)\n- [Bad](javascript:alert(1))\ntext\n* [Nguyen Duc](http://b.dev)'), [
		{ name: 'Nguyễn Đức', url: 'https://a.github.io/x/', slug: 'nguyen-duc' },
		{ name: 'Nguyen Duc', url: 'http://b.dev', slug: 'nguyen-duc-2' },
	]);
});
