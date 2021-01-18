# Track Stack Toolkit (tst)

A tracking toolkit which helps developers and analytics team to:

- Keep analytics tracking information under version control.
- Makes meta-queries possible based on structured data in yaml-files.
- Allow for better feature-attribution per release-cycle.
- Match KPIs to => Events to => Release-cycles.

# Requirements:

- python
- `pip install -U PyYAML`

# Backlog:

- Interface build with jinja, which allows for:
  - macros and templates
  - link-building so that one can view images in the interface
  - render Bigquery queries from event_names in yaml-files
- Tests to make sure event_names, param_names, etc. are the required length.
- Generate swift & java code based on yaml-files which can be copied into developers' code-base directly.
- Integrate with data-build-tool (dbt)

# Feedback:

- Feel free to reach out to me on twitter: @dirkjobosman
