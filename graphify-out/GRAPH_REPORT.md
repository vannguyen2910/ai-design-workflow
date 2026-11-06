# Graph Report - ai-design-workflow  (2026-11-05)

## Corpus Check
- Large corpus: 426 files · ~712,606 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 1276 nodes · 1957 edges · 88 communities (74 shown, 14 thin omitted)
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 402 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Lesson 2 Discover Methods
- Method Cards
- Lesson 3 Insights
- Stage Gates and Export
- Starter Design System
- Data Safety Excerpts
- Research Questions and Stakeholders
- User-Voice Synthesis Flow
- Demo Case Export Script
- Delivery App Case Pack
- Design Pattern Layers
- Deploy Workflow
- Template Export Script
- AI Strengths and Limits
- Hub Builder Script
- Kitchen Crate Case
- Lesson 5 AI Prototyping
- Case Templates
- Lesson 2 Snapshots
- AI in Discover Evidence
- AI Team and Agents
- Site Lesson Overview Script
- Lesson 1 Design Process
- Lesson 3 Brief
- Site Dependencies
- AI Risks and Failure Cases
- Workflow Kit
- Activity Flow and Gates
- Hub Serve Script
- Four Stages and Brief
- Lesson Series Map
- Archived Outlines
- Site Sync Script
- Lesson Details and Access Levels
- Lesson 2 Brief
- Lessons 7 and 8 Measurement
- Program Decisions Log
- Program Brief
- Method and Activity Standards
- AI in Discover Methods
- Simulated respondents too agreeable
- Experience Hub
- Designer Fund AI in Design 2026 survey (
- Gates
- How the Hub Works
- Design decision (D)
- scripts
- _is_sep()
- _is_sep()
- hub.js
- Decision: many errors found
- Stage gates with lettered checks 1a to 4
- Graph
- Graph
- components.html component showcase
- Publish Your Hub Guide
- astro.config.mjs
- Research: Future of UI/UX and design car
- Test report template
- Open questions
- listLessons()
- Course site index.html (hub landing page
- AGENTS.md rules file
- AI-assisted vs AI-generated (AI drafts, 
- Activity flow standard: 12 rules
- AI draft kept separate from verified cop
- AI Design Workflow Plan (7 weeks, 2 sess
- Standard Slide Blocks
- Lesson 2 snapshot: pre-knowledge-restruc
- Hub page: Overview (self-building matrix
- astro/tsconfigs/strict
- Anonymise before AI sees data; quote IDs
- prototype-checkpoint/app.js
- checkpoint-prototype/app.js
- Rule-break hunt instructor answer key
- AI Design Workflow program README
- Accessibility rules
- Delivery App course case (fictional)
- Accessibility rules (WCAG 2.2 AA baselin
- toolkit-refactor-stage.sh
- Shopify: prototype-first, platform not p
- Glossary template
- Principle checks (Nielsen heuristics)
- Glossary

## God Nodes (most connected - your core abstractions)
1. `build()` - 34 edges
2. `Hub Overview (Knowledge Hub)` - 24 edges
3. `build()` - 22 edges
4. `Lesson 1: Your Design Process, with AI` - 22 edges
5. `Lesson details` - 18 edges
6. `AI in Discover` - 18 edges
7. `AI fills gaps with plausible generic content` - 16 edges
8. `Method cards README (index and writing rules)` - 15 edges
9. `Gates` - 14 edges
10. `Course plan` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Flawed AI synthesis of An Ngay` --semantically_similar_to--> `User-Voice Synthesis skills (8 steps)`  [INFERRED] [semantically similar]
  assets/templates/synthesis-hunt/synthesis-an-ngay-ai.md → examples/user-voice-synthesis/step-cards.md
- `Skill (step card) template` --semantically_similar_to--> `Competitor Analysis skills (8 steps)`  [INFERRED] [semantically similar]
  assets/templates/workflow-kit/step-card-template.md → examples/competitor-analysis/step-cards.md
- `Session A teaches, session B practises on own case` --semantically_similar_to--> `Theory, practice, outcome lanes per week`  [INFERRED] [semantically similar]
  _archive/plan-2026-10-22-14-session.md → assets/diagrams/ai-design-workflow-six-weeks.html
- `Seven weekly modules table` --semantically_similar_to--> `Diagram: AI Design Workflow in six weeks (swimlane)`  [INFERRED] [semantically similar]
  _archive/plan-2026-10-22-14-session.md → assets/diagrams/ai-design-workflow-six-weeks.html
- `Data safety: three classes, four habits` --semantically_similar_to--> `Data classes: safe, ask first, never in a public tool`  [INFERRED] [semantically similar]
  lessons/01-design-process-with-ai/materials/_archive/design-process-with-ai-lesson-pre-condense-2026-10-30.md → learning/reference/five-excerpts-answer-key.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **AI in Discover verification guardrails** — _archive_ai_in_discover_2026_10_15_pre_polish2_anonymise_before_paste, _archive_ai_in_discover_2026_10_15_pre_polish2_propose_first, _archive_ai_in_discover_2026_10_18_pre_cleanup_neutral_prompting_sycophancy, _archive_ai_in_discover_2026_10_18_pre_cleanup_after_interview_session_to_quotes, _archive_ai_in_discover_2026_10_18_pre_cleanup_gate_1_extended [INFERRED 0.85]
- **Traceability and measurement chain** — _archive_09_traceability_and_alignment_golden_thread, _archive_09_traceability_and_alignment_alignment_check, _archive_09_traceability_and_alignment_opportunity_solution_tree, _archive_09_traceability_and_alignment_nielsen_heuristics_baseline, _archive_08_measuring_design_success_goals_signals_metrics [EXTRACTED 1.00]
- **Company patterns: design system and principles as AI control layer** — _archive_01_market_research_spotify_encore_mcp, _archive_01_market_research_linear_ai_for_context, _archive_01_market_research_shopify_prototype_first, _archive_01_market_research_figma_mcp_skills_rules [EXTRACTED 1.00]
- **Kitchen Crate discover evidence set** — _archive_demo_case_kitchen_crate_01_discover_sources_anonymised_quotes, _archive_demo_case_kitchen_crate_01_discover_sources_anonymised_competitors_readme, _archive_demo_case_kitchen_crate_00_context_case_card, _archive_demo_case_kitchen_crate_01_discover_scope [INFERRED 0.85]
- **Claude Code memory and handoff practices** — _archive_claude_code_16_lessons_nhat_anh_2026_10_22_claude_md_short, _archive_claude_code_16_lessons_nhat_anh_2026_10_22_three_memory_files, _archive_claude_code_16_lessons_nhat_anh_2026_10_22_handoff_message [EXTRACTED 1.00]
- **Deliver stage working files** — _archive_demo_case_kitchen_crate_04_deliver_test_plan, _archive_demo_case_kitchen_crate_04_deliver_findings, _archive_demo_case_kitchen_crate_04_deliver_handoff, _archive_demo_case_kitchen_crate_04_deliver_measurement_plan [EXTRACTED 1.00]
- **Starter design system and prototype starter** — _archive_demo_case_kitchen_crate_03_develop_prototype_design_system_readme, _archive_demo_case_kitchen_crate_03_develop_prototype_design_system_components, _archive_demo_case_kitchen_crate_03_develop_prototype_project_rules, _archive_demo_case_kitchen_crate_03_develop_prototype_index [EXTRACTED 1.00]
- **Hub pages mirroring stage working files** — _archive_demo_case_kitchen_crate_hub_01_scope, _archive_demo_case_kitchen_crate_hub_02_evidence, _archive_demo_case_kitchen_crate_hub_03_problem_brief [EXTRACTED 1.00]
- **Opportunity to hypothesis to decision/test/metric chain** — _archive_demo_case_kitchen_crate_hub_opportunities_o1, _archive_demo_case_kitchen_crate_hub_hypotheses_h1, _archive_demo_case_kitchen_crate_hub_decisions_d1, _archive_demo_case_kitchen_crate_hub_tests_t1, _archive_demo_case_kitchen_crate_hub_metrics_m1 [EXTRACTED 1.00]
- **Four hub quality gates** — _archive_demo_case_kitchen_crate_gate1, _archive_demo_case_kitchen_crate_gate2, _archive_demo_case_kitchen_crate_gate3, _archive_demo_case_kitchen_crate_gate4 [EXTRACTED 1.00]
- **Hub update cycle: refresh, decide, export** — _archive_demo_case_kitchen_crate_workflow_refresh_hub, _archive_demo_case_kitchen_crate_hub_05_alignment, _archive_demo_case_kitchen_crate_workflow_export_hub [INFERRED 0.75]
- **Discover method cards (competitor analysis, desk research, observation, questionnaire)** — assets_method_cards_01_discover_competitor_analysis, assets_method_cards_01_discover_desk_research, assets_method_cards_01_discover_observation, assets_method_cards_01_discover_questionnaire [INFERRED 0.85]
- **Archived lesson-details versions** — _archive_lesson_details_2026_10_15_en, _archive_lesson_details_2026_10_15_pre_module2_timing, _archive_lesson_details_2026_10_22_14_session [INFERRED 0.85]
- **AI workflow pattern and GitHub flow diagrams** — assets_diagrams_ai_pattern_render, assets_diagrams_ai_pattern_route, assets_diagrams_github_collaboration_workflow, assets_diagrams_github_create_build_push_publish [INFERRED 0.75]
- **Define stage 5-step flow** — assets_method_cards_02_define_01_identify_themes, assets_method_cards_02_define_02_sort_and_cluster, assets_method_cards_02_define_03_define_insights, assets_method_cards_02_define_04_frame_opportunities, assets_method_cards_02_define_05_set_design_challenges [EXTRACTED 1.00]
- **Develop brainstorm methods** — assets_method_cards_03_develop_01_brainstorm_brainwriting, assets_method_cards_03_develop_01_brainstorm_crazy_8s, assets_method_cards_03_develop_01_brainstorm_how_might_we_ideation, assets_method_cards_03_develop_01_brainstorm_opportunity_solution_tree [EXTRACTED 1.00]
- **Develop select methods** — assets_method_cards_03_develop_02_select_concept_sketching, assets_method_cards_03_develop_02_select_impact_vs_effort, assets_method_cards_03_develop_02_select_proposed_process_map, assets_method_cards_03_develop_02_select_storyboarding [EXTRACTED 1.00]
- **Six AI harness terms forming an agent's request-to-answer journey** — assets_references_08_ai_harnesses_infographic_agent_loop, assets_references_08_ai_harnesses_infographic_tool_calling, assets_references_08_ai_harnesses_infographic_context_management, assets_references_08_ai_harnesses_infographic_checkpointing, assets_references_08_ai_harnesses_infographic_permissions_sandboxing, assets_references_08_ai_harnesses_infographic_guardrails [EXTRACTED 1.00]
- **Deliver-stage method cards (test and handoff)** — assets_method_cards_04_deliver_01_test_ab_testing, assets_method_cards_04_deliver_01_test_concept_testing, assets_method_cards_04_deliver_01_test_internal_feedback_session, assets_method_cards_04_deliver_01_test_usability_testing_moderated, assets_method_cards_04_deliver_01_test_usability_testing_unmoderated, assets_method_cards_04_deliver_02_handoff_handoff_pack, assets_method_cards_04_deliver_02_handoff_measurement_plan [EXTRACTED 1.00]
- **Hub narrative pages: Scope, Evidence, Problem brief** — assets_starter_files_case_folder_template_hub_01_scope, assets_starter_files_case_folder_template_hub_02_evidence, assets_starter_files_case_folder_template_hub_03_problem_brief [INFERRED 0.85]
- **Hub traceability chain O-H-D-T-M** — assets_starter_files_case_folder_template_hub_o1, assets_starter_files_case_folder_template_hub_h1, assets_starter_files_case_folder_template_hub_d1, assets_starter_files_case_folder_template_hub_t1, assets_starter_files_case_folder_template_hub_m1 [EXTRACTED 0.90]
- **Artifact templates** — assets_starter_files_case_folder_template_hub_artifacts__templates_competitor_analysis, assets_starter_files_case_folder_template_hub_artifacts__templates_generic, assets_starter_files_case_folder_template_hub_artifacts__templates_ia_sitemap, assets_starter_files_case_folder_template_hub_artifacts__templates_interview_synthesis, assets_starter_files_case_folder_template_hub_artifacts__templates_persona, assets_starter_files_case_folder_template_hub_artifacts__templates_prototype, assets_starter_files_case_folder_template_hub_artifacts__templates_survey_results [INFERRED 0.85]
- **Hub item types O-H-M-D-T chain** — assets_starter_files_case_folder_template_hub_how_the_hub_works_hub_concept_opportunity, assets_starter_files_case_folder_template_hub_how_the_hub_works_hub_concept_hypothesis, assets_starter_files_case_folder_template_hub_how_the_hub_works_hub_concept_decision, assets_starter_files_case_folder_template_hub_how_the_hub_works_hub_concept_test, assets_starter_files_case_folder_template_hub_how_the_hub_works_hub_concept_metric [EXTRACTED 1.00]
- **Stage working files across Discover to Deliver** — assets_starter_files_case_folder_template_learnings_discover_scope, assets_starter_files_case_folder_template_learnings_define_problem_brief, assets_starter_files_case_folder_template_learnings_develop_options, assets_starter_files_case_folder_template_learnings_deliver_findings [INFERRED 0.85]
- **Week 5 prototype starter kit (design system, rules, empty page)** — assets_starter_files_case_folder_template_learnings_prototype_design_system_readme_starter_design_system_notes, assets_starter_files_case_folder_template_learnings_prototype_design_system_components_html_components_page, assets_starter_files_case_folder_template_learnings_prototype_project_rules_project_rules, assets_starter_files_case_folder_template_learnings_prototype_index_html_empty_prototype_page [EXTRACTED 1.00]
- **AI-assisted hub workflows following the step card format** — assets_starter_files_case_folder_template_tools_step_competitor_analysis_workflow, assets_starter_files_case_folder_template_tools_step_user_voice_synthesis_workflow, assets_starter_files_case_folder_template_tools_step_refresh_hub_workflow, assets_starter_files_case_folder_template_tools_step_export_hub_workflow [EXTRACTED 1.00]
- **Fictional Delivery App competitor set** — assets_starter_files_course_case_competitors_dailylarder_daily_larder, assets_starter_files_course_case_competitors_homeharvest_homeharvest, assets_starter_files_course_case_competitors_nibblekit_nibble_kit [EXTRACTED 1.00]
- **Knowledge Hub pages, one per lesson** — assets_templates_hub_scope_scope_page, assets_templates_hub_evidence_evidence_page, assets_templates_hub_problem_brief_problem_brief_page, assets_templates_hub_develop_develop_page, assets_templates_hub_alignment_alignment_page, assets_templates_hub_findings_findings_page, assets_templates_hub_handoff_handoff_page, assets_templates_hub_case_log_case_log_page [EXTRACTED 1.00]
- **Prototype starter kit files** — assets_starter_files_prototype_starter_readme_prototype_starter, assets_starter_files_prototype_starter_design_system_readme_design_system_notes, assets_starter_files_prototype_starter_design_system_components_components_page, assets_starter_files_prototype_starter_index_empty_page, assets_starter_files_prototype_starter_project_rules_rules_file [EXTRACTED 1.00]
- **Delivery App course case materials** — assets_starter_files_course_case_source_notes_delivery_app_notes, assets_starter_files_course_case_source_notes_answer_key_answer_key, assets_starter_files_course_case_persona_ai_draft_busy_first_timer, assets_starter_files_course_case_po_case_pack_delivery_app_pack [INFERRED 0.95]
- **Worked-example activity flows (draft, verify, decide pattern)** — examples_competitor_analysis_step_cards, examples_user_voice_synthesis_step_cards, examples_user_flow_process_map_step_cards [EXTRACTED 1.00]
- **Workflow kit templates** — assets_templates_workflow_kit_step_card_template, assets_templates_workflow_kit_agents_md_starter, assets_templates_workflow_kit_propose_first_card, assets_templates_workflow_kit_prompt_vocabulary, assets_templates_workflow_kit_workflow_hygiene_checklist, assets_templates_workflow_kit_failure_cases [EXTRACTED 1.00]
- **Insight chain: quote > persona > journey map > opportunity > insight hub** — learning_reference_ai_in_insights_persona, learning_reference_ai_in_insights_journey_map, learning_reference_ai_in_insights_opportunity, learning_reference_ai_in_insights_insight_hub, learning_reference_ai_in_insights_four_steps [EXTRACTED 1.00]
- **Evidence against automating a bad workflow** — learning_reference_ai_strengths_and_limits_dont_automate_bad_workflow, learning_reference_ai_strengths_and_limits_ai_amplifier_dora, learning_reference_ai_strengths_and_limits_hammer_obliterate, learning_reference_ai_strengths_and_limits_workslop, learning_quality_and_measurement_product_vs_workflow_measure [INFERRED 0.85]
- **Discover activities following method-first, AI-after** — learning_reference_ai_in_discover_ai_heuristic_evaluator, learning_reference_ai_in_discover_assumption_mapping, learning_reference_ai_in_discover_research_questions, learning_reference_ai_in_discover_method_first_ai_after, learning_reference_ai_in_discover_facilitator_page [INFERRED 0.75]
- **Lesson 1 archived versions** — lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_lesson_2_session_2026_10_22, lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_lesson_delivery_version_2026_10_07, lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_lesson_pre_agent_hub_2026_10_23, lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_lesson_pre_condense_2026_10_30, lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_lesson_pre_practice_at_home_2026_10_30 [EXTRACTED 1.00]
- **Data safety teaching chain** — learning_reference_five_excerpts_answer_key_three_data_classes, lessons_01_design_process_with_ai_assets_five_excerpts_activity, learning_research_vietnam_data_safety_law [INFERRED 0.85]
- **Four core concepts taught in Lesson 1** — lessons_01_design_process_with_ai_materials_design_process_with_ai_lesson_context, lessons_01_design_process_with_ai_materials_design_process_with_ai_lesson_grounding, lessons_01_design_process_with_ai_materials_design_process_with_ai_lesson_hallucination, lessons_01_design_process_with_ai_materials_design_process_with_ai_lesson_ai_assisted_vs_generated [EXTRACTED 1.00]
- **Break the brief: four activities** — lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_activity_order_2026_10_26_research_questions, lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_activity_order_2026_10_26_ux_observation, lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_activity_order_2026_10_26_challenge_assumptions, lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_activity_order_2026_10_26_competitor_analysis [EXTRACTED 1.00]
- **Lesson 1 slide outline version history** — lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_slide_outline_pre_agent_hub_2026_10_23_doc, lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_slide_outline_pre_practice_at_home_2026_10_30_doc, lessons_01_design_process_with_ai_materials__archive_design_process_with_ai_slide_outline_pre_trim_2026_10_30_doc, lessons_01_design_process_with_ai_materials_design_process_with_ai_slide_outline_doc [INFERRED 0.85]
- **Lesson 2 lesson-file revisions (synthesis move, condense, insights)** — lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_synthesis_move_2026_10_30, lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_condense_2026_10_30, lessons_02_discover_the_problem_materials__archive_discover_the_problem_lesson_pre_insights_2026_11_01 [INFERRED 0.95]
- **Lesson 2 slide-outline revisions (synthesis move, trim, insights)** — lessons_02_discover_the_problem_materials__archive_discover_the_problem_slide_outline_pre_synthesis_move_2026_10_30, lessons_02_discover_the_problem_materials__archive_discover_the_problem_slide_outline_pre_trim_2026_10_30, lessons_02_discover_the_problem_materials__archive_discover_the_problem_slide_outline_pre_insights_2026_11_01 [INFERRED 0.95]
- **Early Lesson 2 in-class practice and activity designs superseded by home chain** — lessons_02_discover_the_problem_materials__archive_discover_the_problem_practice_pre_activity_order_2026_10_26, lessons_02_discover_the_problem_materials__archive_discover_the_problem_slide_outline_pre_activity_order_2026_10_26_activity_one_line_each, lessons_02_discover_the_problem_materials__archive_discover_the_problem_slide_outline_pre_knowledge_restructure_2026_10_26_activity_predict_what_ai_finds, lessons_02_discover_the_problem_materials__archive_discover_the_problem_practice_pre_insights_2026_11_01 [INFERRED 0.75]
- **Break the brief activities** — lessons_02_discover_the_problem_materials_discover_the_problem_lesson_scope, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_ux_observation, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_challenge_assumptions, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_research_questions, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_competitor_analysis [EXTRACTED 1.00]
- **Synthesis trust chain** — lessons_02_discover_the_problem_materials_discover_the_problem_lesson_three_steps, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_source_id, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_five_things, lessons_02_discover_the_problem_materials_discover_the_problem_lesson_dissent [EXTRACTED 1.00]
- **Persona to hub chain** — lessons_03_research_you_can_trust_materials__archive_research_you_can_trust_lesson_pre_condense_2026_10_30_persona, lessons_03_research_you_can_trust_materials__archive_research_you_can_trust_lesson_pre_condense_2026_10_30_journey_map, lessons_03_research_you_can_trust_materials__archive_research_you_can_trust_lesson_pre_condense_2026_10_30_opportunity, lessons_03_research_you_can_trust_materials__archive_research_you_can_trust_lesson_pre_condense_2026_10_30_insight_hub [EXTRACTED 1.00]
- **Lesson 3 chain: persona, journey map, opportunity, insight hub, all traced by insight ID** — lessons_03_research_you_can_trust_materials_research_you_can_trust_lesson_persona, lessons_03_research_you_can_trust_materials_research_you_can_trust_lesson_journey_map, lessons_03_research_you_can_trust_materials_research_you_can_trust_lesson_opportunity, lessons_03_research_you_can_trust_materials_research_you_can_trust_lesson_insight_hub [EXTRACTED 1.00]
- **Lesson 4 pipeline: solutions on map, concept sketch, user flow, process map** — lessons_04_explore_ideas_materials_explore_ideas_lesson_opportunity_solution_tree, lessons_04_explore_ideas_materials_explore_ideas_lesson_concept_sketching, lessons_04_explore_ideas_materials_explore_ideas_lesson_user_flow, lessons_04_explore_ideas_materials_explore_ideas_lesson_process_map [EXTRACTED 1.00]
- **Lesson 5 framework: Design Pattern layers, One View, Second View, Gate/Rules/Skill** — lessons_05_ai_prototyping_materials_archive_ai_prototyping_lesson_pre_condense_2026_10_30_design_pattern_four_layers, lessons_05_ai_prototyping_materials_archive_ai_prototyping_lesson_pre_condense_2026_10_30_one_view, lessons_05_ai_prototyping_materials_archive_ai_prototyping_lesson_pre_condense_2026_10_30_second_view, lessons_05_ai_prototyping_materials_archive_ai_prototyping_lesson_pre_condense_2026_10_30_gate_rules_skill [EXTRACTED 1.00]
- **Four layers of Design Pattern** — lessons_05_ai_prototyping_materials_ai_prototyping_lesson_token, lessons_05_ai_prototyping_materials_ai_prototyping_lesson_component, lessons_05_ai_prototyping_materials_ai_prototyping_lesson_shell, lessons_05_ai_prototyping_materials_ai_prototyping_lesson_template [EXTRACTED 1.00]
- **Gate, Rules and Skill control layers** — lessons_05_ai_prototyping_materials_ai_prototyping_practice_gatesae, lessons_05_ai_prototyping_materials_ai_prototyping_lesson_tenrules, lessons_05_ai_prototyping_materials_ai_prototyping_lesson_prototypeskill [INFERRED 0.85]
- **Lesson 5 material set (lesson, practice, outline)** — lessons_05_ai_prototyping_materials_ai_prototyping_lesson_lesson5, lessons_05_ai_prototyping_materials_ai_prototyping_practice_practice5, lessons_05_ai_prototyping_materials_ai_prototyping_slide_outline_deck [EXTRACTED 1.00]

## Communities (88 total, 14 thin omitted)

### Community 0 - "Lesson 2 Discover Methods"
Cohesion: 0.06
Nodes (60): Break the brief (scope + 4 activities), Challenge assumptions (Importance x Evidence), Competitor analysis, Four questions before sending data to AI, Keep dissent on same page as insight, Lesson 2: Discover the Problem, Five things that make an insight sound stronger than it is, Nielsen's 10 usability heuristics (+52 more)

### Community 1 - "Method Cards"
Cohesion: 0.05
Nodes (51): Method card: Interactive prototype, Method card: Proof of concept (POC), Method card: Wireframes, Method card: A/B testing, Method card: Concept testing, Method card: Internal feedback session, I noticed / I wonder / what if feedback format, Method card: Usability testing (moderated) (+43 more)

### Community 2 - "Lesson 3 Insights"
Cohesion: 0.05
Nodes (44): Lesson 3 slide outline, archived pre-trim 2026-10-30 (quote-based, Kitchen Crate), Lesson 3: Turn Research into Insights You Can Trust, Delivery app insight set IN-01 to IN-09 (fictional case), Four questions about AI in research (lead page, time saved, when to skip AI, tool choice), Insight hub (insights/ folder in Knowledge Hub, atomic research), JMIR AI 2024 thematic analysis: 20 min vs 567 min on 40 SMS, Customer journey map with assumption cells, CHI 2024 study: 450 LLM-generated personas biased (Salminen) (+36 more)

### Community 3 - "Stage Gates and Export"
Cohesion: 0.10
Nodes (43): Agreement status (agreed/pending/not available), AI draft kept separate from verified version, Alignment table, tools/export-hub.py deterministic export, Gate 1 Discover, Gate 2 Define, Gate 3 Develop, Gate 4 Deliver (+35 more)

### Community 4 - "Starter Design System"
Cohesion: 0.08
Nodes (37): components.html component showcase page, Starter components (button, field, radio card, card, badge, alert, step indicator), Design tokens (colour, type, spacing, radius, 44px target), Starter design system notes (for AI coding tool), Empty prototype index.html, Project rules file for AI coding tool, Prototype starter (week 5), anonymised folder (evidence with quote IDs) (+29 more)

### Community 5 - "Data Safety Excerpts"
Cohesion: 0.06
Nodes (36): Five Excerpts Answer Key, Data classes: safe, ask first, never in a public tool, T5 Activity Rule-break Hunt, Gate C review and rule check, Three system rules (inventory, tokens, template/shell), Source Verification Lesson 1, Verification grades a/b/c/d, Figma 36/35/29 unverified (+28 more)

### Community 6 - "Research Questions and Stakeholders"
Cohesion: 0.11
Nodes (28): Research questions, 01-discover/scope.md, Stakeholder meetings, User interviews, Identify themes, Sort and cluster, Affinity diagram, Define insights (+20 more)

### Community 7 - "User-Voice Synthesis Flow"
Cohesion: 0.07
Nodes (35): User-voice synthesis, User-voice flow: scope, coding draft, verified coding, themes, opportunities, Problem brief (Define stage), Alignment check, Options and decisions, Checkpoint prototype page (index.html), Checkpoint prototype (week 6), First-box flow: Start, Choose delivery day, Check your first box (+27 more)

### Community 8 - "Demo Case Export Script"
Cohesion: 0.11
Nodes (23): build(), chip(), chips(), doc_html(), prop_table(), resolver(), tnode(), val_html() (+15 more)

### Community 9 - "Delivery App Case Pack"
Cohesion: 0.07
Nodes (28): Persona 'Busy first-timer' (AI draft), Stand-in PO project pack: Delivery App, Weak assumption: people leave because of price, 30-day retention 41% to 50% goal, Source notes answer key (instructor only), Intended themes A-E (date, pause, cooking time, price, variety), Source notes: Delivery App (24 invented notes), Sample bias note (reviews, forum, two interviews) (+20 more)

### Community 10 - "Design Pattern Layers"
Cohesion: 0.08
Nodes (32): How big teams feed AI (Stripe, Atlassian, Vercel, Uber), Component layer, Content voice, Design Pattern (four layers), Gate, Rules and Skill, Layer ladder (fix at the right layer), Lesson 5: AI Prototyping, One View (design-system.html baseline) (+24 more)

### Community 11 - "Deploy Workflow"
Cohesion: 0.07
Nodes (28): runs-on, steps, concurrency, cancel-in-progress, group, environment, needs, runs-on (+20 more)

### Community 12 - "Template Export Script"
Cohesion: 0.13
Nodes (15): Artifact, _aslist(), case_info(), collect(), _csv(), _front(), _ids(), media_kind() (+7 more)

### Community 13 - "AI Strengths and Limits"
Cohesion: 0.11
Nodes (24): AI Strengths and Limits (pre-merge draft), Where AI is strong: bounded, checkable, writing-like tasks, Where AI falls short: long, judgment-heavy, whole real jobs, Automation levels L1/L2/L3, Before You Automate checklist (8 questions), Hammer: Don't Automate, Obliterate (E19), METR task length vs reliability (E18), Remote Labor Index (E16) (+16 more)

### Community 14 - "Hub Builder Script"
Cohesion: 0.17
Nodes (23): build(), art_card(), chip(), chips(), doc_html(), domain_label(), href_for(), icard() (+15 more)

### Community 15 - "Kitchen Crate Case"
Cohesion: 0.10
Nodes (22): Kitchen Crate case card, Kitchen Crate meal-kit app, 30-day retention 41%, Data rules template, Open questions template, Product and users template, Competitor analysis working file, Discover scope template (+14 more)

### Community 16 - "Lesson 5 AI Prototyping"
Cohesion: 0.13
Nodes (24): AI Prototyping lesson brief, Design Pattern = token, component, shell, template, Manual before AI: learner decides shell and template first, One View (reference) and The Second View (real prototype), Rules file: ten laws (five system, five working), Activity: persona with or without insight, Lesson 5 moved details, Activity: Rule-break hunt (three planted violations) (+16 more)

### Community 17 - "Case Templates"
Cohesion: 0.12
Nodes (3): Principle P1, Principle P6, Principle P8

### Community 18 - "Lesson 2 Snapshots"
Cohesion: 0.14
Nodes (21): Kitchen Crate / delivery app quote set (24 quotes with IDs), Lesson 2 snapshot: pre-condense (2026-10-30), Break the brief (scope plus four activities, each producing one hub file), Two-layer quote check (find exact string, read context), Synthesis four steps: Decision, Evidence, Claim, Challenge, Lesson 2 snapshot: pre-insights (2026-11-01), Five things that make an insight sound stronger than it is, Lesson 2 snapshot: pre-synthesis-move (2026-10-26 content) (+13 more)

### Community 19 - "AI in Discover Evidence"
Cohesion: 0.14
Nodes (18): Investigate and Generate archetypes, AI in Discover: evidence and practice by activity, Anonymise before paste, Citation hallucination evidence, Interview consent notice (record, internal use, no sharing), AI in Discover (pre-polish2 version), Facilitator page (HTML interview tool), Propose first, append only (+10 more)

### Community 20 - "AI Team and Agents"
Cohesion: 0.18
Nodes (15): Agent vs a single chat turn, AI team: eight agents across four phases, Three career directions, Context, Lesson 1: Your Design Process, with AI, Grounding, Pre-read brief (Appendix A), Worked example: one task done twice (+7 more)

### Community 21 - "Site Lesson Overview Script"
Cohesion: 0.14
Nodes (8): lessons, wanted, frontmatter(), LESSONS, ROOT, args, push, staged

### Community 22 - "Lesson 1 Design Process"
Cohesion: 0.18
Nodes (17): Your Design Process, with AI brief, AI team: agents per Double Diamond phase, designer leads, Overtime cut order, data safety and activity never cut, Data safety: safe, ask first, never in public tool, Lesson 1 moved details, First agent in five steps; context pack, skill, gate, AGENTS.md, Activity: guess first, then let AI classify five excerpts, Lesson 1: Your Design Process, with AI (+9 more)

### Community 23 - "Lesson 3 Brief"
Cohesion: 0.17
Nodes (17): Turn Research into Insights brief, Homework: synthesis on own quotes into Evidence page, User-voice synthesis: anonymise, quote ID, word for word, unknown allowed, Lesson 3 moved details, Lesson 3 research questions, AI-tagged questions to test on delivery-app insight set, Lesson 3: Insights You Can Trust, Neutral prompting against sycophancy (Ask, Don't Tell) (+9 more)

### Community 24 - "Site Dependencies"
Cohesion: 0.15
Nodes (13): astro, @astrojs/markdown-remark, @astrojs/starlight, sharp, dependencies, astro@^7.2.10, @astrojs/markdown-remark@^7.3.5, @astrojs/starlight@^0.42.7 (+5 more)

### Community 25 - "AI Risks and Failure Cases"
Cohesion: 0.15
Nodes (15): NN/g findings on AI design and synthetic user tools, AI-assisted design risk table with workflow countermeasures, Failure cases and risks, Teaching working designers notes, Teaching hypotheses: one real case, teach the gate, do it by hand first, Levels L1 Automate, L2 Draft + review, L3 Assist, 100 tasks AI can automate (pre-polish), Evidence: gains on bounded tasks, losses on hard familiar work (+7 more)

### Community 26 - "Workflow Kit"
Cohesion: 0.18
Nodes (15): An Ngay quotes set (fictional), Flawed AI synthesis of An Ngay, AGENTS.md starter, Failure cases (five real breakdowns), Prompt vocabulary, Propose-first card, Workflow kit overview, Skill (step card) template (+7 more)

### Community 27 - "Activity Flow and Gates"
Cohesion: 0.16
Nodes (14): Workflow: User Voice Synthesis, User-voice synthesis 8-step flow (Frame, Suggest, Review, Collect, Code, Verify, Synthesise, Interpret), Gates A, B, C (right voices, verbatim traceable, weighted not counted), Method: activity flow standard, step cards, stage gates (pre gate-1 extension), Activity flow rules (frame first, alternate YOU/AI, keep AI draft, max 3 gates), Canonical gate list (4 stage gates, 15 checks 1a-4d), Generate pattern (3 options, select, develop, critique, check, decide), Investigate pattern (Frame, Suggest, Review, Collect, Extract, Verify, Compare, Interpret) (+6 more)

### Community 28 - "Hub Serve Script"
Cohesion: 0.21
Nodes (5): main(), Handler, main(), newest_source(), rebuild_if_needed()

### Community 29 - "Four Stages and Brief"
Cohesion: 0.15
Nodes (13): Four stages: Discover, Define, Develop, Deliver, Hallucination and allowing unknown, Break the brief: four activities, four files, Challenge assumptions, Competitor analysis, Design Principles: UX, business, severity, gates, Discover in the Double Diamond and AI capabilities, Lesson 2: Discover the Problem (archived pre-activity-order) (+5 more)

### Community 30 - "Lesson Series Map"
Cohesion: 0.26
Nodes (14): Data safety block in Lesson 1, Double Diamond stage map, Final project: present your case (session 14), Lesson 1: Your design process, with AI, Lesson 2: Discover the problem, Lesson 3: Turn research into insights you can trust, Lesson 4: Frame the problem worth solving, Lesson 5: Explore ideas and pick a direction (+6 more)

### Community 31 - "Archived Outlines"
Cohesion: 0.19
Nodes (14): Archived outline pre-agent-hub (70 slides, 2026-10-23), Homework: build project folder in about 45 minutes, 27 method reference slides (Discover, Define, Develop, Deliver), Archived outline pre-practice-at-home (36 slides, 2026-10-24), Kitchen Crate running example, Archived outline pre-trim (2026-10-30), Practice 1: seven steps, about 4 hours, Practice 1 at home: build your project folder (+6 more)

### Community 32 - "Site Sync Script"
Cohesion: 0.16
Nodes (9): all, conflicts, list(), missing, skip(), STATE, toDrive, toRepo (+1 more)

### Community 33 - "Lesson Details and Access Levels"
Cohesion: 0.18
Nodes (13): Lesson details (English, 2026-10-15), Lesson details (Vietnamese, pre module-2 timing), Lesson details (Vietnamese, 14-session version with module 2 timing), Three access levels (full, limited, none) and agreement status, Case folder layout (learnings, hub, tools, _personal, AGENTS.md), Lessons 1 to 9 (process, discover, research, frame, explore, prototype, refine, test, handoff), Module 2 time allocation (sessions A and B, 46-minute shortfall), Series Vocabulary (one name per idea) (+5 more)

### Community 34 - "Lesson 2 Brief"
Cohesion: 0.19
Nodes (13): Discover the Problem brief, AI never plays PO or user, Mark metrics confirmed or assumed, agreement status, Lesson 2 moved details, Activity: write insight, cross-critique in pairs, Three-question test for a design principle, Lesson details, Three access levels: full, limited, none (+5 more)

### Community 35 - "Lessons 7 and 8 Measurement"
Cohesion: 0.18
Nodes (13): Hub private by default, four sharing options, Lesson 7: Refine and Check, Lesson 8: Test with Real Users, Quality and measurement, Alignment check (decision to opportunity, hypothesis, principle), Questions to ask product for business metrics, Goals > Signals > Metrics, Knowledge Hub with cross-linked IDs (+5 more)

### Community 36 - "Program Decisions Log"
Cohesion: 0.23
Nodes (9): Decisions log (2026-10-05), Three access levels to product and business (full, limited, none), Case folder with context pack, Class format: teaching session plus practice session each week, Discover without role-play: written stakeholder check and peer interviews, Series plan: decisions and lesson skeleton, Series vocabulary: one name per idea, Vietnam market notes (+1 more)

### Community 37 - "Program Brief"
Cohesion: 0.23
Nodes (11): Program brief, Six program-level learning objectives, Why now: 91% weekly AI use, blurred roles, bottleneck moves to verification, Outcome is a repeatable workflow, not prompts or a tool, Start Discover from business question, not a given brief, Learning Loop applied to the course, learning-log.md proposal, Learning loop gaps: logging and reflection (+3 more)

### Community 38 - "Method and Activity Standards"
Cohesion: 0.26
Nodes (11): Five working-file rules (AI returns only its section, keep AI draft separate), Method: activity flow, skills, gates, Activity flow standard (12 rules), Standard AI instruction checklist, Four stage gates, 20 checks (1a to 4d), Pattern B: Generate, Hard-stop checks 1b, 1c, 1f, Pattern A: Investigate (+3 more)

### Community 39 - "AI in Discover Methods"
Cohesion: 0.27
Nodes (12): AI in Discover, AI as second heuristic evaluator, human severity, Assumption mapping, importance x evidence, Citation hallucination (3-13% URLs, 14-95% citations), Facilitator page (HTML interview tool), Method first, AI after (review, do, AI, compare), Research questions vs interview questions, Vietnamese transcript accuracy unmeasured, 10-minute test (+4 more)

### Community 40 - "Simulated respondents too agreeable"
Cohesion: 0.24
Nodes (12): Simulated respondents too agreeable, LLM-generated persona bias (CHI 2024), Rules file drifts from code, AI strengths, limits, task catalogue, AI amplifies strengths and weaknesses (DORA 2025), Where AI falls short: long tasks, judgment, synthetic users, Before-you-automate checklist (8 questions), Do not automate a bad workflow (+4 more)

### Community 41 - "Experience Hub"
Cohesion: 0.20
Nodes (11): Experience Hub, Measuring design success, Goals, Signals, Metrics framework, HEART framework, PO question kit, Measuring AI workflow quality (time, error rate, rework), Alignment check, Traceability and alignment (+3 more)

### Community 42 - "Designer Fund AI in Design 2026 survey ("
Cohesion: 0.18
Nodes (10): Designer Fund AI in Design 2026 survey (906 designers, 91% weekly AI use), Method: activity flow standard (pre stage regroup, six working stages), Six working stages (Frame, Explore, Shape, Prototype, Validate, Hand off) mapped to four gates, Research: Market, Risks, Vietnam, Teaching (pre-merge), Company workflows: Spotify Encore MCP, Linear, Shopify, Figma, Failure cases and risks table (satisficing, synthetic users, deskilling, tool sprawl), Teaching working designers: seven hypotheses, Vietnam market (low-confidence salary bands, validation plan) (+2 more)

### Community 43 - "Gates"
Cohesion: 0.20
Nodes (11): Gates, Four gates (Discover, Define, Develop, Deliver), Hard stop checks (1b, 1c, 1f), Traceability (decision back to user need), Data rules, Anonymised source data and data rules, Alignment check, Recorded trade-off (pulls against) (+3 more)

### Community 44 - "How the Hub Works"
Cohesion: 0.24
Nodes (11): How the Hub Works, Hub (markdown project folder / final report), One source of truth principle, Refresh / generated blocks, Hub warnings (computed by script), Hub HTML report (index.html), Hash-routed HTML report with 5 views, Journey pages 01-scope to 07-handoff (+3 more)

### Community 45 - "Design decision (D)"
Cohesion: 0.31
Nodes (11): Design decision (D), Hypothesis (H), Item files (O,H,M,D,T), Metric (M), Opportunity (O), Test (T), Problem brief, Handoff (+3 more)

### Community 46 - "scripts"
Cohesion: 0.18
Nodes (11): scripts, astro, build, dev, prebuild, predev, prestart, preview (+3 more)

### Community 47 - "_is_sep()"
Cohesion: 0.31
Nodes (4): _is_sep(), Renderer, stash_link(), build()

### Community 48 - "_is_sep()"
Cohesion: 0.31
Nodes (4): _is_sep(), Renderer, stash_link(), build()

### Community 49 - "hub.js"
Cohesion: 0.31
Nodes (7): cell(), direct(), esc(), href(), link(), reach(), safe()

### Community 50 - "Decision: many errors found"
Cohesion: 0.36
Nodes (10): Decision: many errors found, Decision: is the source ID real, Decision: does the source say it, Flowchart: check an AI-returned insight, Step: log the error and fix against the original, Step: rerun with a tighter prompt, Swimlane: three steps of working with AI, Step 3 Challenge: AI critiques, learner keeps or changes the insight (+2 more)

### Community 51 - "Stage gates with lettered checks 1a to 4"
Cohesion: 0.25
Nodes (8): Stage gates with lettered checks 1a to 4d, Market research, Draft six-stage workflow with gates (Frame to Hand off), Figma: MCP, skills and rules files, Linear: AI for context, not taste, Spotify: design system as AI infrastructure via MCP, Stage methods and delegation, Mixed gate by stage: evidence, principles, real users, buildability

### Community 54 - "components.html component showcase"
Cohesion: 0.31
Nodes (8): components.html component showcase, Accessibility rules (4.5:1, 44px targets, keyboard, focus), Components (button, field, radio card, card, badge, alert, steps), Starter design system notes, Design tokens (colour, type, spacing, radius, touch target), Prototype index.html empty page, Project rules file for AI coding tool, Prototype starter (week 5)

### Community 55 - "Publish Your Hub Guide"
Cohesion: 0.22
Nodes (8): Publish Your Hub Guide, GitHub Pages publishing, Tools to bring, Outcome Examples (Travel Buddy), AI Design Workflow program introduction, Double Diamond (Discover, Define, Develop, Deliver), Knowledge Hub, Landing page preview and edit guide

### Community 56 - "astro.config.mjs"
Cohesion: 0.36
Nodes (7): lessons, PAGE_ID, pageId(), relativeUrl(), remarkLinks(), rewrite(), walk()

### Community 57 - "Research: Future of UI/UX and design car"
Cohesion: 0.32
Nodes (8): Research: Future of UI/UX and design careers with AI (Vietnamese, archived), BLS web and digital designer outlook (+7% 2024-2034; +5% 2025-2035), Career paths: strategic generalist, designer-builder, AI product designer, Confidence marks (verified, secondary-only, weak) on every figure, Data safety sources (Law 91/2025/QH15, Decree 356/2025/ND-CP, consumer vs enterprise training policy), Figma State of the Designer 2026 (36/35/29 split), NN/g State of UX in 2026, Stanford 'Canaries in the Coal Mine' (early-career job decline 16%)

### Community 58 - "Test report template"
Cohesion: 0.29
Nodes (8): Test report template, User flow template, Artifacts (project documents), Findings, Results against baseline, Findings weighted by importance, Test plan, System Usability Scale (SUS)

### Community 59 - "Open questions"
Cohesion: 0.25
Nodes (8): Open questions, Product and users, 'assumed' labelling for unconfirmed facts, Competitor analysis, Scope, Agreement status (agreed/pending/not available), User-voice synthesis, AI draft vs verified sections

### Community 60 - "listLessons()"
Cohesion: 0.32
Nodes (6): listLessons(), CARD, m, CARD, markCurrent(), onRequest

### Community 61 - "Course site index.html (hub landing page"
Cohesion: 0.48
Nodes (6): Course site index.html (hub landing page), Render consented hub cards, Course site README, GitHub Pages hosting, hubs.js consent registry, Student hub (one public link per student)

### Community 62 - "AGENTS.md rules file"
Cohesion: 0.29
Nodes (6): AGENTS.md rules file, Data safety: safe, ask first, never in a public tool, Knowledge Hub, Project folder layout, Activity: predict then let AI sort five excerpts, Slide: The Knowledge Hub

### Community 63 - "AI-assisted vs AI-generated (AI drafts, "
Cohesion: 0.29
Nodes (6): What AI is good at and where it falls short, Program intro slide outline (5 slides), Slide: track progress with KNOW, DO, SHOW, Slide: learning rhythm, Slide: problem, mission and vision (draft), Slide: six-week roadmap

### Community 64 - "Activity flow standard: 12 rules"
Cohesion: 0.40
Nodes (6): Activity flow standard: 12 rules, Standard AI instruction checklist, Activity flow standard, Three levels: stage map, activity flow, step card, Step card template, Step card format and quality checklist

### Community 65 - "AI draft kept separate from verified cop"
Cohesion: 0.33
Nodes (5): Handout: AI Design Workflow Step 1 (90-minute practice session), Activity 3: Baseline run (manual vs agent comparison), Appendix A/B: fake 'An Ngay' interview dataset with planted traps, Activity 2: Role card template for an agent, Activity 1: Workflow audit (score tasks by repeat, clear I/O, checkable)

### Community 66 - "AI Design Workflow Plan (7 weeks, 2 sess"
Cohesion: 0.40
Nodes (5): AI Design Workflow Plan (7 weeks, 2 sessions a week), Session A teaches, session B practises on own case, Seven weekly modules table, Diagram: AI Design Workflow in six weeks (swimlane), Theory, practice, outcome lanes per week

### Community 67 - "Standard Slide Blocks"
Cohesion: 0.33
Nodes (6): Standard Slide Blocks, Definition slide block (What/Why/When), notes-audit before teaching, Vietnamese Voice Sample, Competitor analysis method card sample, Vietnamese voice rules (no filler, English headings)

### Community 68 - "Lesson 2 snapshot: pre-knowledge-restruc"
Cohesion: 0.40
Nodes (5): Lesson 2 snapshot: pre-knowledge-restructure (earliest, 2026-10-22 content), Business question, outcome, metric, baseline and shared scope with agreement status, Heuristic evaluation with AI and Nielsen severity 0-4, Slide outline snapshot: 25 slides, pre-knowledge-restructure, Activity: predict what AI will find, then score (18 min)

### Community 69 - "Hub page: Overview (self-building matrix"
Cohesion: 0.40
Nodes (5): Hub page: Overview (self-building matrix), Four gates with lettered checks, Item IDs (O, H, D, P, T, M), Knowledge Hub template, Hub sharing and privacy guidance

### Community 70 - "astro/tsconfigs/strict"
Cohesion: 0.40
Nodes (4): astro/tsconfigs/strict, exclude, extends, include

### Community 71 - "Anonymise before AI sees data; quote IDs"
Cohesion: 0.50
Nodes (4): Anonymise before AI sees data; quote IDs (R01, I01-01), Method card: Desk research, Method card: Observation (shadowing), Method card: Questionnaire (survey)

### Community 74 - "Rule-break hunt instructor answer key"
Cohesion: 0.67
Nodes (4): Rule-break hunt instructor answer key, Three planted rule breaks, Rule-break hunt screen (Chon thoi gian giao), Starter design system tokens and components

### Community 75 - "AI Design Workflow program README"
Cohesion: 0.83
Nodes (3): AI Design Workflow program README, AI Design Workflow program: 12 sessions in 6 weeks, one project, one reusable workflow, one Knowledge Hub, Student workspace template repo (separate repo)

### Community 76 - "Accessibility rules"
Cohesion: 0.67
Nodes (3): Accessibility rules, WCAG 2.2 AA baseline, Design system notes

### Community 77 - "Delivery App course case (fictional)"
Cohesion: 0.67
Nodes (3): Delivery App course case (fictional), SUMMARY site page list, Method Cards library by Double Diamond stage

## Ambiguous Edges - Review These
- `D3.md` → `O1.md`  [AMBIGUOUS]
  assets/starter-files/case-folder-template/hub/D3.md · relation: conceptually_related_to

## Knowledge Gaps
- **222 isolated node(s):** `astro/tsconfigs/strict`, `Stage methods and delegation`, `Failure cases and risks`, `Vietnam market notes`, `Teaching working designers notes` (+217 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 357 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Workflow card index` connect `Stage Gates and Export` to `Activity Flow and Gates`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `build()` (e.g. with `resolver()` and `_natkey()`) actually correct?**
  _`build()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `astro/tsconfigs/strict`, `Stage methods and delegation`, `Failure cases and risks` to the rest of the system?**
  _222 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Lesson 2 Discover Methods` be split into smaller, more focused modules?**
  _Cohesion score 0.05875706214689266 - nodes in this community are weakly interconnected._
- **Why does `Workflow: User Voice Synthesis` connect `Activity Flow and Gates` to `Lesson Details and Access Levels`, `Stage Gates and Export`?**
  _High betweenness centrality (0.011) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `build()` (e.g. with `resolver()` and `_natkey()`) actually correct?**
  _`build()` has 2 INFERRED edges - model-reasoned connections that need verification._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `D3.md` and `O1.md`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._