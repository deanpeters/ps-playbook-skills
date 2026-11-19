# Maintaining the download files

These notes are for people changing the library. To use the Playbook, start with the [download guide](README.md).

## Rebuild downloads


From the source repository root, rebuild the shared references, then the ZIPs. Python 3 is sufficient; no API keys or model sessions are used.

```bash
python3 projects/build.py
```

```bash
python3 downloads/build.py
```

Check the ZIPs against current sources without writing:

```bash
python3 downloads/build.py --check
```

Run the archive tests:

```bash
python3 -m unittest discover -s downloads -p 'test_*.py'
```

The builder creates six skill-and-prompt bundles, six Claude plugin packages, and one Project kit. It preserves source skill and prompt bytes, includes the license, uses reproducible ZIP metadata, and refuses unexpected ZIPs. Readmes and manifests are generated packaging material. The Project kit's setup guide changes its repository-only skill link to a web link for portability. The build does not install, publish, or upload the packages.


## Rebuild the shared reference kit


For maintainers working in the source repository: Python 3 only; no additional packages or API keys. The downloadable Project kit does not include the build scripts. These commands write or check local files, not live assistant setups.

```bash
python3 projects/build.py
```

```bash
python3 projects/build.py --check
```

```bash
python3 -m unittest discover -s projects -p 'test_*.py'
```

Edit the source skills/prompts, then rebuild. Do not edit uploads/ by hand. New Plays require updating skills/README.md and the title mapping in build.py. The shared capture contract lives in project-instructions.md under **Shared interaction contract**, ending before **Play boundaries**; keep its copies aligned with skills and prompt wrappers. Keep compact instructions behaviorally consistent and within 7,700 characters, including whitespace and newlines. The build enforces the limit and checks consistency, references, ordering, and prompt inclusion.

Packaging checks do not establish platform installation, live behavior, sharing access, or Productside approval.

## Plugin format validation

All six plugin manifests and expected skill discovery passed strict local validation with Claude Code 2.1.328 before the documentation update. This does not establish live installation or behavior.
