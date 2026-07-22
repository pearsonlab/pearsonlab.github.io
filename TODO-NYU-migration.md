# Duke → NYU migration to-do list

Every Duke-specific reference on the site, grouped so you can decide what to
change and when. Items are `file:line` and clickable in most editors.

**What's already done in this branch** (visual rebrand):

- Color scheme swapped from Duke Blue `#001A57` → NYU Violet `#57068C`
  (navbar, buttons, jumbotron), with Deep Violet `#330662` accents.
- Navbar painted NYU Violet.
- Header banner (jumbotron) chapel photo → NYU violet gradient.
- Duke Neurobiology logo → placeholder NYU CNS lockup (`images/nyu_cns_lockup.svg`).
- Bold "We're moving to NYU (Sept 1, 2026)" announcement on the landing page.

Everything below still needs a human decision (timing, facts, or per-person
choices), so it's left for you.

---

## 1. Site identity & metadata  *(decide when to flip — you're still at Duke until Sept 1)*

- [ ] `_config.yml:1` — title: `"Pearson Lab at Duke University"` → NYU
- [ ] `_config.yml:3` — description: "Computational neuroscience at Duke University…" → NYU
- [ ] `index.html:4` — desc: "The online home of the Pearson Lab at Duke University" → NYU
- [ ] **Get the official NYU / CNS lockup.** The current logo is a typographic
      placeholder. Official NYU wordmark/seal is trademarked and can't be
      hotlinked — request an approved asset from **brand@nyu.edu** or CNS /
      Arts & Science communications, then replace `images/nyu_cns_lockup.svg`.

## 2. People & contact info — `_data/people.yml`

Emails: decide per person who is moving; update the movers to `@nyu.edu`.

- [ ] `:38` John — `john.pearson@duke.edu`
- [ ] `:61` Ganchao Wei — `ganchao.wei@duke.edu`
- [ ] `:101` Trevor Alston — `trevor.alston@duke.edu`
- [ ] `:116` David St-Amand — `david.st-amand@duke.edu`
- [ ] `:129` Shiyang Pan — `shiyang.pan@duke.edu`
- [ ] `:143` Caitlin Lewis — `caitlin.lewis@duke.edu`
- [ ] `:209` Miles Martinez — `miles.martinez@duke.edu`
- [ ] `:227` Ziyi Gong — `ziyi.gong@duke.edu`

Bios (update present-tense affiliations; past training at Duke is historical and can stay):

- [ ] `:44–46` John's bio — Duke postdoc / DIBS / current appointments. Add the
      NYU Center for Neural Science appointment.
- [ ] `:77` "joint with Warren Grill" links to `bme.duke.edu` — update if the
      joint appointment changes at NYU.
- [ ] `:104` Trevor — "sixth-year Neurobiology graduate student at Duke"
- [ ] `:113` David — headshot hosted on `scholars.duke.edu` (may break if the
      Duke Scholars profile is removed; consider self-hosting the image).
- [ ] `:133` Shiyang — "at Duke"
- [ ] `:147` Caitlin — "…Engineering at Duke"
- [ ] `:213` Miles — "entered Duke through the CNAP program"

Alumni outcomes — historical, **likely keep as-is**:

- `:251` "Duke Computer Science (PhD program)", `:303` "Duke Medical School",
  `:321` Duke Hart Leadership Fellow.

## 3. Recruiting / how to join — `join_us.md`  *(biggest rewrite)*

The entire PhD-pathways section is Duke-specific and needs rewriting for NYU
(e.g. CNS PhD program, and whichever cross-listed programs apply):

- [ ] `:14` intro paragraph ("Duke provides a wonderful environment…")
- [ ] `:16` Neurobiology (neuro.duke.edu) — → NYU CNS
- [ ] `:18` Cognitive Neuroscience Admitting Program (CNAP / DIBS / CCN)
- [ ] `:20` Biostatistics & Bioinformatics (biostat.duke.edu)
- [ ] `:22` Psychology & Neuroscience (psychandneuro.duke.edu)
- [ ] `:24` Electrical & Computer Engineering (ece.duke.edu)
- [ ] `:46` undergraduate research (undergraduateresearch.duke.edu)
- [ ] `:58–60` minors / high-school policy — references Duke rules & DUNE program

## 4. Location — `location.md` + `images/location/`

Entirely about the Bryan Research Building at Duke → Meyer Building,
**4 Washington Place, New York, NY 10003** (CNS is in Meyer, room ~621).

- [ ] `:7` Bryan Research Building + `maps.duke.edu` link
- [ ] `:9,:13,:17,:21` all four location photos are Duke buildings
      (`images/location/bryan_ext.jpg`, `bryan_ent.jpg`, `admin_ent.jpg`,
      `ctn_ent.jpg`) — replace with NYU/Meyer photos
- [ ] Rewrite the walking directions (breezeway, Center for Theoretical
      Neurobiology, etc.) for the new building.

## 5. Learning resources — `learning.md`  *(low priority; generalize or update)*

- [ ] `:62` "the intro Bayesian class at Duke"
- [ ] `:64` Cliburn Chan's STA 663 (a Duke course)
- [ ] `:73` "Duke uses this for its intro ML class"

## 6. Research collaborators — `_data/research.yml`  *(accurate external links; review)*

Duke collaborator lab links — keep if the collaborations continue, update/remove
if they don't:

- `:26,:28` Eva Naumann lab · `:50,:52` Richard Mooney lab · `:59,:63` Greg Field lab
  (all `neuro.duke.edu`).

## 7. Blog posts — `_posts/`  *(historical news — review, most likely KEEP)*

These accurately describe past events at Duke and normally shouldn't be
rewritten. Only revisit if a link rots or you want to note the affiliation
change. Duke references appear in:
`2015-11-06-news_pearson_profile.md`, `2015-11-13-big-data-nih.md`,
`2015-12-19-pnas_paper.md`, `2016-01-01-new_commentary_pnas.md`,
`2016-3-10-nasher_eye_tracking.md`, `2016-4-6-opencv-videos.md`,
`2016-4-8-in-the-news.md`, `2016-9-9-time-allocation-in-neuro.md`,
`2017-1-14-aws-grant.md`, `2017-3-31-modeling-other-minds.md`,
`2017-4-18-job-ad.md` (has `john dot pearson at duke dot edu`),
`2018-9-12-artificial-agents-social-decisions.md`,
`2018-10-30-high-throughput-legal-decisions.md`,
`2018-12-5-incubator-award.md`, `2019-1-16-poster-award.md`,
`2019-10-29-vae-preprint.md`, `2020-08-20-grad-school.md`,
`2015-11-06-eye_tracking_tech.md`, `2015-11-06-announcing_plab.md`.
Several also hotlink `people.duke.edu/~jmp33` / `~sni` assets that may
eventually disappear — consider self-hosting those images.

## 8. Housekeeping / leftover assets

- [ ] `images/chapel_gradient.jpg` — no longer referenced (jumbotron is now a
      gradient). Delete once you're happy with the new header.
- [ ] `images/DUSOM_Dept_Neurobio_stack.jpg` — old Duke Neurobiology logo, now
      unused. Delete after confirming the new lockup.
- [ ] `.image-size-overrides` / `.html5validator.yaml` / `lychee.toml` — check
      these don't still whitelist the removed images or dead Duke links.
