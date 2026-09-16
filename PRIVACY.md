# Privacy Notes

Life OS is designed as a local-first personal feedback system.

## Default data path

The MVP uses SQLite on the machine where the application runs. A deployed instance would therefore store data on the server instead of on the user's device.

## Sensitive inputs

Activity logs can reveal personal routines. Avoid committing database files, exports, screenshots, or copied personal records to the repository.

## Future export features

Exports should be explicit and user-controlled. Documentation should make the destination and format clear before data leaves local storage.

## Product principle

Useful analytics do not require collecting more personal data than the feature needs. New fields should have a clear purpose, validation rule, and retention story before being added.
