# flakywatch

<div align="center">
  <img src="assets/banner.svg" alt="flakywatch project banner" width="100%"/>
  <br/>
  ![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
  ![Status](https://img.shields.io/badge/Status-Early%20Development-F59E0B?style=for-the-badge)
</div>

> Find intermittently failing tests by combining JUnit XML reports from repeated test runs.

## Why it exists

A focused, inspectable starter for a real developer workflow. It favors explicit behavior, local execution, and small pieces that are easy to understand and extend.

## Features

- Reads multiple JUnit XML report files
- Groups test cases by class and test name
- Flags tests that both pass and fail across runs
- Exports a concise JSON report for CI

## Architecture

```mermaid
flowchart LR
  A[Local input] --> B[flakywatch]
  B --> C[Validation and core logic]
  C --> D[Readable report]
  C --> E[CI exit status]
```

## Requirements

- Python 3.10+ / standard library
- A terminal and a local checkout of this repository

## Quick start

```bash
python src/flakywatch.py reports/*.xml
```

## Example

```bash
python src/flakywatch.py reports/ --json
```

## Project status and limitations

This repository contains an initial working implementation, not a production-certified product. Review the source and test it against your own fixtures before adopting it in critical workflows.

A test is flagged only when the supplied reports contain both a pass and a failure for the same class/name pair.

## Roadmap

- [ ] Add duration variance analysis
- [ ] Support more report dialects
- [ ] Add baseline comparison between CI runs

## Contributing

Issues and pull requests are welcome. Include a small reproducible example for bug reports, keep changes focused, and add tests for new behavior. Do not submit secrets or private data.

## License

MIT. See [LICENSE](LICENSE). Third-party services or optional dependencies remain subject to their own terms.
