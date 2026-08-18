# Updates needed in your desktop master database

The new canonical file (`canonical/vocab.json`) mirrors your master, with the
two corrections below already applied downstream (web app, iPhone app). Make
the same two edits in your desktop master so it stays the source of truth:

## 1. ἅγιος — wrong chapter

- **Change chapter from 10 to 9.**
- Position it third in chapter 9: after ἀγαπητός, before αἰώνιος (9-3).
- (In the sequence numbering, ἅγιος is now 77; αἰώνιος through τρίτος shifted
  to 78–92, and chapter 10 now starts at εἰ = 93.)

## 2. κρείττων — corrupted entry

- Current (broken font markup): `κρείττων, ον,<Ε& γεν., </Ε&ονος`
- **Corrected to:** `κρείττων, ον, γεν. ονος`

---

# For your review — differences found in the iPhone app's old data

Tyler's app database had variant lexical forms for a few words. The canonical
file keeps **your master's forms** (the app was regenerated to match), so no
action is needed — but if you prefer any of the app's versions, update your
master and vocab.json together:

| Master (kept) | App had (discarded) |
|---|---|
| οὐ, οὐκ, οὐχ | οὐ (οὐκ, οὐχ) |
| ἐκ, ἐξ | ἐκ (ἐξ) |
| ἕνεκεν | ἕνεκα or ἕνεκεν |
| ἐξομολογέομαι | ἐξομολογέω |
| κρείττων, ον, γεν. ονος | κρείσσων, -ονος |
| μέχρι | μέχρι or μέχρις |
| ὀψία, -ας, ἡ | ὄψιος, -α, -ον |
| ἄρχω | ἄρχομαι |

One word existed **only** in the app and is now dropped: **εἰ μή** (chapter
10, "if not; except"). If it belongs in the vocabulary, add it to your master
and to vocab.json.

The app also **gained 13 words** it had been missing (they were in your
master all along): αἰώνιος, ἀπεκρίθη, μου (ch 9); φῶς (11); ἑαυτοῦ, μακάριος
(13); οὕτως (14); καρπός (19); ἀπέρχομαι, γράφω (23); φόβος (35); δέομαι,
ἐμπαίζω, μανθάνω, μέλει, ὡσαύτως and other ch-99 extras.

---

# Going forward

- **canonical/vocab.json** in the flashworks repo is now the single source
  for the web app and the iPhone app.
- After you update your desktop master, tell Claude what changed (or hand
  over a fresh export) — the canonical file gets updated and
  `python3 canonical/build.py` pushes it everywhere.
- The iPhone app picks up data changes with its **next App Store build**.
