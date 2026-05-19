import re

path = r"c:\Users\mkaouari\Documents\training-platform\portfolio islam\portfolio.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Remove TMPL_* variable declarations and the TMPL_MAP/loader block ─────
# They start with "    // Inline template srcdoc content" and end before
# "    const translations"
content = re.sub(
    r'    // Inline template srcdoc content.*?(?=\n    const translations)',
    '',
    content,
    flags=re.DOTALL
)

# Also remove data-tmpl attributes from inline iframes (we'll keep them blank)
content = content.replace(' data-tmpl="ACCEUIL"', '')
content = content.replace(' data-tmpl="PARCOURS"', '')
content = content.replace(' data-tmpl="P01"', '')
content = content.replace(' data-tmpl="P02"', '')

# ── 2. Replace the entire openModal function ──────────────────────────────────
NEW_OPEN_MODAL = r'''    function openModal(kind) {
      if (kind === "p1-preview") {
        modalTitle.textContent = "Google Sites LMS (Platform Preview)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Google Sites LMS (Platform Overview)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Platform Structure</h2>
  <p>The LMS is a 4-level hierarchy built in Google Sites, designed for enterprise category management training.</p>
  <div class="grid">
    <div><div class="chip">Accueil</div><p style="font-size:13px">Landing page with brand identity and entry CTAs</p></div>
    <div><div class="chip">Parcours</div><p style="font-size:13px">Catalog of 3 learning tracks with entry points</p></div>
    <div><div class="chip">Module Pages</div><p style="font-size:13px">Per-parcours modules with resources and quiz access</p></div>
    <div><div class="chip">Resources</div><p style="font-size:13px">Embedded Slides, Docs, and Sheets for lesson content</p></div>
  </div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Learning Tracks</h2>
  <div class="grid">
    <div><div class="chip">ABG</div><p style="font-size:13px">Assortiment Base Gestion: core category management methodology</p></div>
    <div><div class="chip">Assort'impact</div><p style="font-size:13px">Business impact-driven assortment decisions with adaptive missions</p></div>
    <div><div class="chip">Store Adaptor</div><p style="font-size:13px">Local adaptation of national assortment strategy</p></div>
    <div><div class="chip">Fil Rouge</div><p style="font-size:13px">Capstone adaptive missions across all tracks</p></div>
  </div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Screenshots</h2>
  <p>Page-level screenshots of the live Google Sites platform can be added here. The templates used to build each page are available in the workspace and can be shared on request.</p>
  <p style="font-size:13px;color:#888;font-style:italic">The platform is an internal tool; direct access is not available publicly. Screenshots are provided for portfolio review only.</p>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "p1-explainer") {
        modalTitle.textContent = "Google Sites LMS (Case Study and Full Workflow)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Google Sites LMS (Carrefour Learning Platform)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Context and Problem</h2>
  <p>Carrefour's category management teams needed a structured internal training tool. The existing onboarding process was fragmented across emails and documents with no scalable delivery mechanism. The goal: build a premium, self-serve learning platform using only Google Workspace tools at zero external cost.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Platform Architecture (4-Level Hierarchy)</h2>
  <ul>
    <li><strong>Level 1 (Accueil):</strong> Landing page with brand identity, CTA to discover the learning tracks, and overview of available content.</li>
    <li><strong>Level 2 (Parcours):</strong> Catalog view listing 3 learning tracks with entry points and progress context.</li>
    <li><strong>Level 3 (Module Pages):</strong> Per-parcours module listings with learning objectives, embedded resources, and quiz access points.</li>
    <li><strong>Level 4 (Resources):</strong> Embedded Google Slides, Docs, and Sheets for lesson content and business case studies.</li>
  </ul>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Technical Approach</h2>
  <p>Google Sites does not support custom HTML natively. To achieve premium visual design, each page was built as a standalone HTML/CSS file (in the workspace under <code>google-sites-lms/templates/</code>), then embedded into Google Sites via the HTML embed gadget.</p>
  <ul>
    <li>Custom CSS with brand color tokens, responsive grid layouts, and card components</li>
    <li>Navigation links wired between pages for cohesive UX flow</li>
    <li>Business use-case cards with scenario prompts embedded in parcours pages</li>
    <li>Script-assisted rebuild pipeline to regenerate slide assets on demand</li>
    <li>Adaptive Fil Rouge missions integrated at the end of each parcours as capstone assessment</li>
  </ul>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Pages Delivered</h2>
  <div class="grid">
    <div><div class="chip">ACCUEIL.html</div><p style="font-size:13px">Home page with CTA and platform overview</p></div>
    <div><div class="chip">PARCOURS.html</div><p style="font-size:13px">Catalog of 3 learning tracks with entry points</p></div>
    <div><div class="chip">P01.html</div><p style="font-size:13px">ABG track: modules and resources</p></div>
    <div><div class="chip">P02.html</div><p style="font-size:13px">Assort'impact track: use-cases and adaptive missions</p></div>
  </div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Impact</h2>
  <ul>
    <li>Accelerated onboarding for category management teams with structured self-serve content</li>
    <li>Fully embedded in Google Workspace: no external tools, no cost, no IT dependency</li>
    <li>Reusable template architecture: adding new tracks requires only duplicating a template file</li>
    <li>Premium visual quality comparable to paid LMS platforms</li>
  </ul>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Confidentiality</h2>
  <p>All materials shown are sanitized. Learner data, internal links, and sensitive business content have been removed. The architecture and design patterns are fully shareable.</p>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "p2-preview") {
        modalTitle.textContent = "Apps Script (Architecture Diagram and Code)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Apps Script Certification System (Architecture)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">End-to-End Trigger Flow</h2>
  <div style="background:#111820;border-radius:14px;padding:18px;overflow-x:auto;">
    <div style="display:flex;flex-wrap:wrap;align-items:center;gap:8px;font-family:monospace;font-size:13px;color:#e7eefb;line-height:2.2">
      <span style="background:#1e3a5f;padding:6px 12px;border-radius:8px;">Google Form Submit</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#1e3a5f;padding:6px 12px;border-radius:8px;">onFormSubmit(e)</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#1e3a5f;padding:6px 12px;border-radius:8px;">normalizeSubmission()</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#1a4a2e;padding:6px 12px;border-radius:8px;">QUIZ_ATTEMPTS sheet</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#1a4a2e;padding:6px 12px;border-radius:8px;">MODULE_PROGRESS sheet</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#1a4a2e;padding:6px 12px;border-radius:8px;">PARCOURS_PROGRESS sheet</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#4a2020;padding:6px 12px;border-radius:8px;">isEligibleForCertificate()</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#4a2020;padding:6px 12px;border-radius:8px;">generateCertificatePdf()</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#3a1a4a;padding:6px 12px;border-radius:8px;">Drive storage</span>
      <span style="color:#64b5f6;">&#8594;</span>
      <span style="background:#3a1a4a;padding:6px 12px;border-radius:8px;">Gmail notification</span>
    </div>
  </div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Data Architecture (Google Sheets)</h2>
  <div class="grid">
    <div><div class="chip">QUIZ_ATTEMPTS</div><p style="font-size:13px">Append-only log of all quiz submissions: scores, timestamps, module IDs, user emails</p></div>
    <div><div class="chip">MODULE_PROGRESS</div><p style="font-size:13px">Upserted row per user/module: best score, completion flag, attempt count</p></div>
    <div><div class="chip">PARCOURS_PROGRESS</div><p style="font-size:13px">Rolled-up completion % per user per parcours, drives certificate eligibility</p></div>
    <div><div class="chip">CERTIFICATES_LOG</div><p style="font-size:13px">Audit trail of issued certificates: user, date, Drive file ID</p></div>
  </div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Main Entry Point</h2>
  <pre>function onFormSubmit(e) {
  const payload = normalizeSubmission(e);
  appendQuizAttempt(payload);
  upsertModuleProgress(payload);
  upsertParcoursProgress(payload);
  if (isEligibleForCertificate(payload.userEmail)) {
    generateCertificatePdf(payload.userEmail);
  }
}</pre>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Dashboard Visibility API</h2>
  <pre>function getProgressDashboardData(payload) {
  const viewer = getViewerContext(payload);
  const scopedRows = applyVisibilityScope(viewer, payload);
  return buildDashboardResponse(scopedRows);
}</pre>
  <p style="font-size:13px">Role-based scoping: learners see only their own data; managers see their team within their assigned perimeter.</p>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "p2-explainer") {
        modalTitle.textContent = "Apps Script (Full Workflow Explained)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Apps Script Certification and Progress System (Full Workflow)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Problem Statement</h2>
  <p>The LMS had no automated way to track quiz results, update learner progress, or issue certificates. Everything was manual: trainers checked Form responses individually, updated spreadsheets by hand, and sent certificates via email. This created delays, inconsistencies, and a poor learner experience.</p>
  <p><strong>Goal:</strong> build a zero-touch pipeline handling the entire lifecycle from quiz submission to certificate delivery with no human steps required.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Step 1 (Form Trigger and Normalization)</h2>
  <p>A Google Forms quiz submission fires an installable <strong>onFormSubmit(e) trigger</strong> via Apps Script. The raw form event contains unstructured response data. <code>normalizeSubmission(e)</code> parses it into a clean, typed payload with user email, module ID, parcours ID, score, timestamp, and answers.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Step 2 (Logging to QUIZ_ATTEMPTS)</h2>
  <p><code>appendQuizAttempt(payload)</code> appends a new row to the QUIZ_ATTEMPTS sheet. Design choice: append-only, not upsert. Every attempt is preserved for analytics, retake tracking, and compliance auditing. Best scores are computed from this log, not overwritten.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Step 3 (Module Progress Upsert)</h2>
  <p><code>upsertModuleProgress(payload)</code> finds or creates the user/module row in MODULE_PROGRESS and updates best score, attempt count, completion flag (when score is at or above the configurable passing threshold), and last attempt timestamp.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Step 4 (Parcours Rollup)</h2>
  <p><code>upsertParcoursProgress(payload)</code> reads all module completion flags for the user in this parcours and recalculates the overall completion %. The PARCOURS_PROGRESS row is always in sync after every quiz submission with no batch jobs needed.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Step 5 (Certificate Generation Pipeline)</h2>
  <p>When <code>isEligibleForCertificate()</code> returns true, the generation pipeline runs:</p>
  <ol>
    <li>Certificate template (Google Slides) duplicated via Drive API</li>
    <li>Slides API replaces name, track, and date placeholders</li>
    <li>Filled deck exported as PDF via Drive export URL</li>
    <li>PDF saved to learner's Drive folder</li>
    <li>Certificate emailed to the learner as an attachment</li>
    <li>Entry written to CERTIFICATES_LOG for audit</li>
  </ol>
  <pre>function generateCertificatePdf(userEmail) {
  const learner = getLearnerProfile(userEmail);
  const copy = DriveApp.getFileById(CERT_TEMPLATE_ID)
    .makeCopy("Certificate_" + learner.name);
  const slides = SlidesApp.openById(copy.getId());
  slides.replaceAllText("{LEARNER_NAME}", learner.name);
  slides.replaceAllText("{PARCOURS_NAME}", learner.parcours);
  slides.replaceAllText("{DATE}", formatDate(new Date()));
  slides.saveAndClose();
  const pdfBlob = DriveApp.getFileById(copy.getId())
    .getAs("application/pdf");
  const pdfFile = DriveApp.getFolderById(CERTS_FOLDER_ID)
    .createFile(pdfBlob);
  logCertificate(userEmail, pdfFile.getId());
  GmailApp.sendEmail(userEmail, "Your certificate",
    "Congratulations! Your certificate is available.",
    { attachments: [pdfBlob] });
}</pre>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Step 6 (Dashboard and Visibility Scoping)</h2>
  <p>A separate Apps Script Web App serves a progress dashboard. <code>getViewerContext()</code> identifies the caller role. Learners see only their own data; managers see their team within their perimeter. This prevents data leakage without requiring a separate auth system.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Impact</h2>
  <ul>
    <li>100% automated end-to-end: zero manual steps from quiz to certificate</li>
    <li>Real-time progress tracking across all parcours and modules</li>
    <li>Scalable to any number of learners with no additional overhead</li>
    <li>Full audit trail preserved for compliance and reporting</li>
    <li>Built entirely within Google Workspace: no external dependencies or costs</li>
  </ul>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "p3-preview") {
        modalTitle.textContent = "Adaptive Assessment (Sample Mission Flow)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Fil Rouge Mission (Sample Flow)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">What is a Fil Rouge Mission?</h2>
  <p>A scenario-based assessment where the learner takes on a business role and makes a series of decisions. Unlike a quiz, there are no universally correct answers: the quality of each decision is evaluated relative to the learner's selected role and business context.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Entry Step (Role and Context Selection)</h2>
  <p>Before the mission starts, the learner selects:</p>
  <ul>
    <li><strong>Role:</strong> Operational, Strategic, or Data-Driven</li>
    <li><strong>Business scope:</strong> Local, Regional, or National</li>
  </ul>
  <p>These two choices determine which scenario data is displayed, which options are available at each decision point, and what "good judgment" looks like for the rest of the mission.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Mission Structure</h2>
  <ol>
    <li><strong>Situation brief:</strong> A realistic business situation is described with relevant data (performance gaps, supplier context, budget constraints).</li>
    <li><strong>Decision point 1:</strong> Choose from 3-4 options, each representing a different business approach.</li>
    <li><strong>Consequence:</strong> The scenario evolves based on your choice, unlocking new data and framing the next decision.</li>
    <li><strong>Decision point 2:</strong> A follow-up decision that depends on what was decided earlier.</li>
    <li><strong>Debrief:</strong> Contextual feedback explains the trade-offs of the path taken, calibrated to the learner's role.</li>
  </ol>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Adaptive Logic</h2>
  <p>The same mission runs differently for different learners. A learner in the Operational role receives different feedback than one in the Strategic role for the same decision, because the expected priorities and trade-offs differ by role. No two learners receive the same feedback path.</p>
</div>`
        );
        modalNote.textContent = "The actual mission content uses sanitized business scenarios. No live or sensitive data is exposed.";
      } else if (kind === "p3-explainer") {
        modalTitle.textContent = "Fil Rouge Missions (How We Built It)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Fil Rouge Adaptive Assessment (Design and Build Process)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">The Problem with Traditional Quizzes</h2>
  <p>Standard quizzes measure memory, not judgment. For category management roles, what matters is decision-making quality in context. A learner who scores 90% on a multiple-choice quiz might still make poor decisions in real situations.</p>
  <p><strong>Goal:</strong> design an assessment where context, complexity, and decision pathways adapt to the learner's role and business environment.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Design Principles</h2>
  <ul>
    <li><strong>Persona-based entry:</strong> Learner selects their role (Operational, Strategic, Data-Driven). This shapes which options are available and what good judgment looks like.</li>
    <li><strong>Perimeter selection:</strong> Local, Regional, or National scope changes the scenario data, supplier landscape, and KPIs shown.</li>
    <li><strong>Branching decisions:</strong> Earlier choices affect what options appear later, creating realistic consequence chains.</li>
    <li><strong>Contextual feedback:</strong> Not correct/incorrect but a business explanation of the implications of the choice in the given context.</li>
  </ul>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Build Process</h2>
  <ol>
    <li><strong>Mission scripting:</strong> Each mission written as a scenario tree: root context, 2-3 decision points, branching outcomes per persona.</li>
    <li><strong>Content design:</strong> Scenario data sanitized from real category work to feel authentic without exposing sensitive information.</li>
    <li><strong>UX integration:</strong> Embedded in the Google Sites parcours pages as interactive cards; learners navigate via button clicks.</li>
    <li><strong>Scoring logic:</strong> Apps Script tracks decision path quality using a weighted rubric per persona, not just the final answer.</li>
    <li><strong>Feedback library:</strong> Pre-written contextual feedback blocks for each decision combined with persona and perimeter.</li>
  </ol>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">LMS Integration</h2>
  <p>Fil Rouge missions serve as the capstone assessment at the end of each parcours. They plug into the same Apps Script pipeline as standard quizzes, so progress tracking, completion flags, and certificate eligibility all work identically.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Why This Is Innovative</h2>
  <p>Most corporate LMS platforms use static quizzes. This adaptive mission framework is inspired by simulation-based learning used in executive education, built entirely within Google Workspace at near-zero cost, making it accessible for teams without specialized simulation software budgets.</p>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "p4-preview") {
        modalTitle.textContent = "CUPRA Storytelling Deck";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.src = "https://drive.google.com/file/d/1KnAZdf4w3QED5qSAed5IaNqLUJQP1akG/preview";
        modalNote.textContent = "CUPRA deck preview from Google Drive. If the embed is blocked, the deck is available directly via Google Drive.";
      } else if (kind === "p4-explainer") {
        modalTitle.textContent = "CUPRA Deck (How It Was Made)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "CUPRA Storytelling Deck (Process and Context)",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Academic Context</h2>
  <p>This deck was created as a solo deliverable for a strategic marketing course at Albert School Paris. The brief: select a brand, analyze its positioning, and build a decision-oriented presentation suitable for the brand's executive team.</p>
  <p>CUPRA was chosen for its compelling strategic position: a premium-sporty sub-brand of SEAT/Volkswagen Group forging its own identity against established players like Alfa Romeo, BMW M-series, and Hyundai N-line.</p>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Deck Objectives</h2>
  <ul>
    <li>Establish CUPRA's brand identity and current market positioning</li>
    <li>Analyze competitive landscape and whitespace opportunities</li>
    <li>Build a compelling narrative arc from problem to strategic recommendation</li>
    <li>Demonstrate premium visual design with consistent brand voice</li>
  </ul>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Build Process</h2>
  <ol>
    <li><strong>Research:</strong> Market data, brand positioning maps, consumer perception analysis, competitive benchmarking across the sports compact segment</li>
    <li><strong>Narrative structure:</strong> Built using the Problem / Stakes / Solution / Proof / Call to Action consulting framework</li>
    <li><strong>Visual design:</strong> CUPRA's brand colors (copper and dark tones), bold typography, performance-focused imagery, all built from scratch in Google Slides</li>
    <li><strong>Writing:</strong> Executive-quality copy: concise, high-impact, zero filler slides. Each slide earns its place in the story.</li>
    <li><strong>Iteration:</strong> 3 complete versions reviewed against the brief before final submission</li>
  </ol>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">What Makes It Stand Out</h2>
  <p>Most student decks are information dumps. This one is built like a consulting deck: visuals support the argument rather than decorating it, the narrative drives toward a clear decision, and the final slide ends with a specific actionable recommendation rather than a generic summary.</p>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "p5-preview") {
        modalTitle.textContent = "Finance Deck Preview";
        modalFrame.style.display = "block";
        modalFrame.srcdoc = "";
        modalFrame.src = "https://drive.google.com/file/d/1uVL7r5iFuv7D1jKrJYvmUC51umVGlItd/preview";
        modalNote.textContent = "Finance deck preview from Google Drive. If Drive blocks embedding, open directly via Google Drive.";
      } else if (kind === "p5-explainer") {
        modalTitle.textContent = "Business Presentations (Gallery Overview)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Finance Deck and Business Presentation Gallery",
          `<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Finance Project Deck</h2>
  <p>A financial analysis presentation built for a business strategy course. Covers company valuation methodology, financial ratio analysis, and investment thesis construction. Demonstrates the ability to translate dense financial data into a decision-oriented narrative for non-finance audiences.</p>
  <div class="chip">Financial Analysis</div><div class="chip">Valuation</div><div class="chip">Investment Thesis</div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Business Analysis Narratives</h2>
  <p>A series of presentations built across different courses, each following a consistent approach: frame the business context, define the problem clearly, present data-driven insights, and close with an actionable recommendation. Topics include market entry analysis, competitive strategy, and operational efficiency.</p>
  <div class="chip">Business Cases</div><div class="chip">Data Storytelling</div><div class="chip">Strategy Frameworks</div>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Visual Design Philosophy</h2>
  <ul>
    <li><strong>Minimal text per slide:</strong> slides are a visual support, not a reading document</li>
    <li><strong>Data visualization:</strong> charts built to communicate a point, not just display numbers</li>
    <li><strong>Brand-aligned color palettes:</strong> each deck uses a palette appropriate to its context</li>
    <li><strong>Executive summary first:</strong> every deck opens with a one-slide key takeaway</li>
  </ul>
</div>
<div class="panel">
  <h2 style="font-size:18px;margin:0 0 8px">Availability</h2>
  <p>The Finance Deck is available for preview via Google Drive. Additional decks from the gallery can be shared on request.</p>
</div>`
        );
        modalNote.textContent = "";
      } else if (kind === "finance") {
        modalTitle.textContent = "Finance Deck Preview";
        modalFrame.style.display = "block";
        modalFrame.srcdoc = "";
        modalFrame.src = "https://drive.google.com/file/d/1uVL7r5iFuv7D1jKrJYvmUC51umVGlItd/preview";
        modalNote.textContent = "This deck opens in an iframe preview. If Drive blocks embedding, use the direct file link from your Google Drive permissions.";
      } else if (kind === "site-home") {
        modalTitle.textContent = "Google Sites Home";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc("Google Sites Home (Preview)", `<div class="panel"><p>Screenshot of the Google Sites home page can be added here. The template file is available in the workspace under <code>google-sites-lms/templates/ACCEUIL.html</code>.</p></div>`);
        modalNote.textContent = "";
      } else if (kind === "site-parcours") {
        modalTitle.textContent = "Parcours Catalogue";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc("Parcours Catalogue (Preview)", `<div class="panel"><p>Screenshot of the parcours catalog page can be added here. The template file is available in the workspace under <code>google-sites-lms/templates/PARCOURS.html</code>.</p></div>`);
        modalNote.textContent = "";
      } else if (kind === "site-abg") {
        modalTitle.textContent = "Parcours ABG";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc("Parcours ABG (Preview)", `<div class="panel"><p>Screenshot of the ABG parcours page can be added here. The template file is available in the workspace under <code>google-sites-lms/templates/P01.html</code>.</p></div>`);
        modalNote.textContent = "";
      } else if (kind === "site-assort") {
        modalTitle.textContent = "Parcours Assort'impact";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc("Parcours Assort'impact (Preview)", `<div class="panel"><p>Screenshot of the Assort'impact parcours page can be added here.</p></div>`);
        modalNote.textContent = "";
      } else if (kind === "cupra") {
        modalTitle.textContent = "CUPRA Storytelling Deck";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.src = "https://drive.google.com/file/d/1KnAZdf4w3QED5qSAed5IaNqLUJQP1akG/preview";
        modalNote.textContent = "CUPRA deck preview from Google Drive.";
      } else if (kind === "workflow") {
        modalTitle.textContent = "Apps Script Workflow Overview";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Apps Script Workflow",
          `<div class="panel"><p><strong>Flow:</strong> Google Form submit &#8594; onFormSubmit(e) &#8594; QUIZ_ATTEMPTS &#8594; MODULE/PARCOURS_PROGRESS &#8594; certificate PDF &#8594; Drive/Gmail.</p><pre>function onFormSubmit(e) {
  const payload = normalizeSubmission(e);
  appendQuizAttempt(payload);
  upsertModuleProgress(payload);
  upsertParcoursProgress(payload);
  if (isEligibleForCertificate(payload.userEmail)) {
    generateCertificatePdf(payload.userEmail);
  }
}</pre></div>`
        );
        modalNote.textContent = "Workflow diagram and code snippet.";
      } else if (kind === "case-study") {
        modalTitle.textContent = "Google Sites LMS (Case Study)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Google Sites LMS (Carrefour Learning)",
          `<div class="panel"><p>Confidential internal learning platform built with Google Sites and Google Workspace. Architecture and design patterns are shareable; sensitive content has been removed.</p></div>`
        );
        modalNote.textContent = "";
      } else if (kind === "mission") {
        modalTitle.textContent = "Fil Rouge Missions (Adaptive Assessment)";
        modalFrame.style.display = "block";
        modalFrame.src = "about:blank";
        modalFrame.srcdoc = makeDoc(
          "Fil Rouge Missions",
          `<div class="panel"><p>A scenario-based adaptive assessment model where context and decision pathways adapt to the learner's role and business perimeter.</p></div>`
        );
        modalNote.textContent = "";
      }
'''

# Find and replace the openModal function
# It starts with "    function openModal(kind) {" and ends with "    }" before "    function closeModal() {"
pattern = r'    function openModal\(kind\) \{.*?(?=\n    function closeModal\(\))'
match = re.search(pattern, content, flags=re.DOTALL)
if match:
    print(f"Found openModal function at chars {match.start()}-{match.end()}")
    content = content[:match.start()] + NEW_OPEN_MODAL.rstrip() + content[match.end():]
    print("Replaced openModal function")
else:
    print("ERROR: Could not find openModal function")

# Also fix the site-preview-grid iframes in the body that were set to src="about:blank"
# Add back simple placeholder text if any are blank
# (they were already set to about:blank and data-tmpl was removed, so they'll show blank)
# Replace them with a simple description div instead
content = content.replace(
    '<iframe class="site-preview-frame" src="about:blank" title="Google Sites home preview"></iframe>',
    '<div class="site-preview-frame" style="display:flex;align-items:center;justify-content:center;background:#f4f7fc;color:#888;font-size:13px;padding:20px;text-align:center">Screenshot to be added<br><span style="font-size:11px">ACCEUIL.html template available in workspace</span></div>'
)
content = content.replace(
    '<iframe class="site-preview-frame" src="about:blank" title="Parcours catalogue preview"></iframe>',
    '<div class="site-preview-frame" style="display:flex;align-items:center;justify-content:center;background:#f4f7fc;color:#888;font-size:13px;padding:20px;text-align:center">Screenshot to be added<br><span style="font-size:11px">PARCOURS.html template available in workspace</span></div>'
)
content = content.replace(
    '<iframe class="site-preview-frame" src="about:blank" title="Parcours ABG preview"></iframe>',
    '<div class="site-preview-frame" style="display:flex;align-items:center;justify-content:center;background:#f4f7fc;color:#888;font-size:13px;padding:20px;text-align:center">Screenshot to be added<br><span style="font-size:11px">P01.html template available in workspace</span></div>'
)
content = content.replace(
    "<iframe class=\"site-preview-frame\" src=\"about:blank\" title=\"Parcours Assort'impact preview\"></iframe>",
    '<div class="site-preview-frame" style="display:flex;align-items:center;justify-content:center;background:#f4f7fc;color:#888;font-size:13px;padding:20px;text-align:center">Screenshot to be added<br><span style="font-size:11px">P02.html template available in workspace</span></div>'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done. Final size: {len(content):,} bytes")
