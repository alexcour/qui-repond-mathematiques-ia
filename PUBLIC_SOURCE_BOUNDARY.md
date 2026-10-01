# Public/private source boundary

This repository intentionally does not redistribute private conversations, private email, or internal reports.

For public sources, `data/sources_v1.1.2.csv` keeps the public locator. For non-public sources, it keeps only a stable `source_id`, access class, date, source type and analytical role, while replacing the locator by `NOT_REDISTRIBUTED::<source_id>`.

Free-text event notes were also reduced where an internal filename, message timestamp or other nonessential private locator was unnecessary for the scientific event representation.

This allows third parties to audit the transition structure without turning a private working corpus into publication of correspondence.
