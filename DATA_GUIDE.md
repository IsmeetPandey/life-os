# Data Guide

Life OS records small daily observations so trends can be reviewed over time.

## What is recorded

The MVP stores daily activity values in a local SQLite database. Recorded minutes are validated before being saved, and the interface can show today's totals and the number of historical observations.

## Interpreting the data

A higher value for an activity is an observation, not automatically a better outcome. Compare like-for-like periods and look for repeated patterns before drawing conclusions.

## Why local SQLite

Keeping the MVP local makes the storage model easy to inspect and keeps the default data path on the user's machine. Future export features should make the data portable without changing the basic local-first model.

## Future analysis

Trend charts, target tracking, weekly reviews, and uncertainty-aware comparisons should build on the same validated records. Any statistical relationship should be presented as an association unless a stronger causal design supports a causal claim.
