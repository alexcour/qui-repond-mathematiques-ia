# Reproducibility

Python 3.10+; standard library only. Run commands from the repository root.

```bash
python3 scripts/verify_release.py
```

Expected final line: RELEASE VERIFICATION: OK. The command runs the 517 structural checks, four mutation tests, descriptive counts, frozen-byte and metadata checks, then the integrity manifest. This is the local verification suite.

```bash
python3 scripts/check_release_ready.py
```

The default publication gate requires an actually verified public manuscript archive and the recorded author's manuscript licence decision. Following the HAL non-acceptance notification dated 26 October 2026, this gate remains pending. The already published package remains available. Use `python3 scripts/check_release_ready.py --documentation-only` for consistency of a documentation correction; success in that mode does not establish manuscript publication or authorize a new release.

To enter actual metadata, use prepare_metadata.py. It changes documentation and citation metadata only; it does not modify historical CSVs or analytical scripts. Obtain the genuine notice and rights decision first. See metadata/PUBLICATION_CONFIG.json. After metadata changes:

```bash
python3 scripts/verify_release.py --write-manifest
python3 scripts/verify_release.py
python3 scripts/check_release_ready.py
```

The manifest excludes itself, the current generated test report and transient Python or Git files. The previous v1.0.0 report is included and checked against its retained fingerprint. To refresh the current test report, redirect a fresh successful verification to TEST_REPORT_v1.1.0.txt; the private enclosing transmission manifest must then be regenerated if that enclosing pack is to be reused.

The package reproduces public corpus structure and descriptive counts. It cannot reconstruct private source bytes, replay the unavailable case-B experiment, establish causal effects or validate every mathematical statement. Keep negative and uncertain outcomes visible.
