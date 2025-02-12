# Split Tests into Different Days

There are times when we want to split tests into different days of the
week. Some tests will be run on Monday, yet others will be run on Tuesday
and so on.

One way to achieve this objective is to mark tests with markers
such as `Monday`, `Tuesday`, ... `Sunday`. Then we implement the
`pytest_runtest_setup()` hook to skip those tests which are not meant
for today.
