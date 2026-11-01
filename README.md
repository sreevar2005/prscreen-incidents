# prscreen-incidents

A small web shop where every `incident/...` branch recreates one **real, documented** security
incident, for trying [prscreen](https://github.com/sreevar2005/pr_Sentinel_final). Each branch is one
commit on top of `main`; its commit message explains the incident and links the sources.

**Nothing here is meant to be run.** Every payload is an inert stand-in, credentials are fake,
and the code recreates only each incident's key mechanism, not the attackers' code.

## Scan it

```bash
git clone https://github.com/sreevar2005/prscreen-incidents
```

Then in the prscreen GUI choose **Git repository**, enter the folder, press **Load branches** and
pick a branch. Or from the command line:

```bash
prscreen scan --repo prscreen-incidents --git main...incident/codecov-2021
```

## Branches

| Branch | Incident | Year | Sources |
| --- | --- | --- | --- |
| `control/ordinary-change` | Control: an ordinary change, should stay quiet | | |
| `incident/toyota-2022` | Toyota T-Connect: access key left in a public repository | 2022 | [GitGuardian](https://blog.gitguardian.com/toyota-accidently-exposed-a-secret-key-publicly-on-github-for-five-years/), [Security Affairs](https://securityaffairs.com/136915/data-breach/toyota-motor-corporation-data-leak.html) |
| `incident/event-stream-2018` | event-stream: a new dependency with an encrypted payload | 2018 | [Black Duck](https://www.blackduck.com/blog/malicious-dependency-supply-chain.html), [Security Affairs](https://securityaffairs.com/78464/hacking/tainted-event-stream-version.html) |
| `incident/ua-parser-js-2021` | ua-parser-js: hijacked package with an install-time downloader | 2021 | [CERT-EU advisory 2021-057](https://www.cert.europa.eu/publications/security-advisories/2021-057/), [CrowdStrike](https://www.crowdstrike.com/en-us/blog/crowdstrike-customers-protected-from-compromised-npm-package-in-supply-chain-attack/) |
| `incident/crossenv-2017` | crossenv: a one-typo package that stole environment variables | 2017 | [The Register](https://www.theregister.com/security/2017/08/03/this-typosquatting-attack-on-npm-went-undetected-for-2-weeks/1282093), [GitLab advisory database](https://advisories.gitlab.com/pkg/npm/crossenv/) |
| `incident/ctx-2022` | ctx (PyPI): a hijacked package that sent out every environment variable | 2022 | [BleepingComputer](https://www.bleepingcomputer.com/news/security/popular-python-and-php-libraries-hijacked-to-steal-aws-keys/), [BleepingComputer (follow-up)](https://www.bleepingcomputer.com/news/security/hacker-says-hijacking-libraries-stealing-aws-keys-was-ethical-research/) |
| `incident/codecov-2021` | Codecov: CI pipelines piping a remote script into bash | 2021 | [BleepingComputer](https://www.bleepingcomputer.com/news/security/codecov-starts-notifying-customers-affected-by-supply-chain-attack/), [CPO Magazine](https://www.cpomagazine.com/cyber-security/codecov-supply-chain-attack-remained-undetected-for-months-and-potentially-affected-major-companies-including-google-ibm-hp-and-others/) |
| `incident/pytorch-2022` | PyTorch nightly: dependency confusion through an extra index | 2022 | [SC Media](https://www.scworld.com/analysis/popular-machine-learning-framework-pytorch-compromised-with-malicious-dependency), [Security Affairs](https://securityaffairs.com/140228/hacking/pytorch-confusion-attack.html) |
| `incident/ultralytics-2024` | Ultralytics: a branch name injected into a privileged workflow | 2024 | [LWN.net](https://lwn.net/Articles/1001215/), [William Woodruff (zizmor)](https://blog.yossarian.net/2024/12/06/zizmor-ultralytics-injection) |
| `incident/tj-actions-2025` | tj-actions/changed-files: a movable tag repointed to malicious code | 2025 | [CISA alert](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction), [The Hacker News](https://thehackernews.com/2025/03/github-action-compromise-puts-cicd.html) |
| `incident/trojan-source-2021` | Trojan Source: invisible characters that reorder code (research) | 2021 | [BleepingComputer](https://www.bleepingcomputer.com/news/security/trojan-source-attack-method-can-hide-bugs-into-open-source-code/), [Wikipedia: Trojan Source](https://en.wikipedia.org/wiki/Trojan_Source) |
