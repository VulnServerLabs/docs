# Git hooks

`pre-commit` scans your **staged** changes with [gitleaks](https://github.com/gitleaks/gitleaks)
and blocks the commit if it finds a secret (API key, token, private key, `.env` value).
CI runs the same scan on every push and pull request (`.github/workflows/security.yml`),
but the hook stops the secret before it ever enters a commit.

## One-time setup (per computer)

```powershell
winget install --id Gitleaks.Gitleaks      # Windows; macOS: brew install gitleaks
gitleaks version                           # restart GitHub Desktop / terminal first if not found
```

## One-time setup (per clone)

```powershell
git config core.hooksPath .githooks
```

GitHub Desktop runs the hook automatically. If gitleaks is missing, the hook blocks the commit
and prints how to install it.

## When it blocks a commit

- **Real secret:** unstage/remove it, move it to Secrets Manager or a local ignored file, and rotate it
  if it was ever pushed.
- **False positive:** copy the `Fingerprint` line from the output into `.gitleaksignore`
  (one per line) or, for values that are public by design, add an allowlist to `.gitleaks.toml`.
