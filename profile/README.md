# erupt

[erupt](https://www.erupt.xyz) is a low-code framework for Java: annotate a class, get the admin — tables, forms, search, permissions, no frontend code. The framework itself lives at [erupts/erupt](https://github.com/erupts/erupt) ([docs](https://docs.erupt.xyz)); this organization holds what is built on it.

Every repository below is an erupt module or application: add the dependency to an erupt app, or run it on its own with `mvn spring-boot:run`.

<!-- repos:start -->
| Repository | What it is |
|---|---|
| [erupt-k8s-dashboard](https://github.com/erupt-io/erupt-k8s-dashboard) | A ready-made Kubernetes admin for erupt in under 2,000 lines of code: pods, deployments, statefulsets, daemonsets, services, configmaps, events, namespaces and nodes, with logs, a web terminal, scaling, restarts and YAML editing. Add the dependency, get the menu. |
| [erupt-miniapp](https://github.com/erupt-io/erupt-miniapp) | A WeChat Mini Program admin for erupt: users and sign-in, subscribe messages and the template library, codes and links, content checks, live rooms, inbox and statistics. Pick the app in the page header; every page follows it. |
| [erupt-pm](https://github.com/erupt-io/erupt-pm) | Project management on erupt: projects, iterations, tasks with sub-tasks, dependencies and milestones, worklogs and a risk register. The same task table as a board, gantt, calendar, timeline or table; pick the project in the page header and every screen follows it. |
| [erupt-report](https://github.com/erupt-io/erupt-report) | Moved: erupt-report is open source inside erupts/erupt (erupt-plugin/erupt-report). This repository only points there. |
| [erupt-sms](https://github.com/erupt-io/erupt-sms) | SMS across vendors for erupt on SMS4J: channels, templates, sending with a log, verification codes and a blacklist, plus a fluent Java API. Pick the channel in the page header; every page follows it. |
| [erupt-talent](https://github.com/erupt-io/erupt-talent) | Recruiting on erupt, end to end: resumes, screening, interview rounds, offers with approval and e-mail, candidate confirmation, onboarding and a hiring funnel. Mailbox capture, offer mail and DingTalk calendar are configured in the admin, not in files. |
| [erupt-wechat](https://github.com/erupt-io/erupt-wechat) | A WeChat Official Account admin for erupt: fans, tags, menus, auto replies, materials, drafts and publishing, template and mass messages, customer service and statistics. Pick the account in the page header; every page follows it. |
<!-- repos:end -->

The list is rebuilt every day from the organization's public repositories by [sync-readme.py](../scripts/sync-readme.py).
