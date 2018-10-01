# GitHub Project Management

Here is stack of rules what recommended to use for making cyber•Congress great again.
As a public open source organization with high-level goals and values we need to delivering transparent information for community.


## Pull request and issue formalization

#### Issue. Once again.

Please-please-please describe your issue! If issue name doesn't explain what should be done please make a good explanation of issue.
Attaching files and links is good way for describing what you want.

#### Issue + New Branch + PR = Awesome!

If you start working with issue you can fork a separate branch from master (or another branch) and work with it. After your work is done make a PR and assign it to
review-competent teammates. After successful PR approval please merge and delete this branch. For good PR you can use [PR template](https://github.com/cybercongress/congress/blob/master/.github/PULL_REQUEST_TEMPLATE.md) with checklist which helps you to get in.

#### For what?!

PR and issue formalization processes eliminate you from extra work with changelog, community, process manager, teammates and also help you to quickly find key changes.

## Tag and release formalization (for repo's maintainers)

Full documentation about Semantic Versioning Specification (SemVer) you can explore [here](https://semver.org/spec/v2.0.0.html).
In general we need to tag versions with it. Git propose it with [CLI](https://git-scm.com/book/en/v2/Git-Basics-Tagging) and [GUI](https://help.github.com/articles/working-with-tags/).
Also tagging is available on GitKraken.

Given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when you make incompatible changes

- MINOR version when you add functionality in a backwards-compatible manner

- PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are [available as extensions](https://semver.org/spec/v2.0.0.html#semantic-versioning-specification-semver) to the MAJOR.MINOR.PATCH format.

#### For what?!

Automatic changelog generator is in process of attaching to each repo. This script parses tags and releases to compile beautiful changelog.


## Docs decorating

All documentation about repo you should keep at `/docs` folder. Automatic script will collect all docs in knowledge and deploy them to https://cybersearch.io/ .
For now there are few requirements to keep docs:

- store you docs in `/docs` folder in your repo;
- if you want to publish them at knowledge commit all docs changes in `master`;
- add `about $repo_name$.md` to your docs;
- Update table of content in your docs in `$repo_name.yml` file. PLEASE keep indenting!;
- keep your documentation in actual state.

## Templates

We developed issues, PR, Contributing and Code of Conduct templates to formalize communication inside/outside the team.
All what you need is clone `/.github` folder form congress repo ([link](https://github.com/cybercongress/congress/tree/master/.github))
and customize it for your repo if it necessary.


## Gitcoin

Guide to initiate gitcoin process is [here](https://github.com/cybercongress/congress/blob/master/community/README.md#gitcoin).
If you need to fund some issue from repo that you maintain just add `community: gitcion` label to issue that you want to
fund. Also you can fund issues in another open source projects.

If you fund issues from `cyber•Congress` repo attach [gitcoin banner](https://github.com/cybercongress/cyber-search/blob/master/README.md#gitcoin-tasks) to your `README.md` file in `master`.
The easiest way to do it is just attach following code:
```
## Gitcoin Tasks
<a href="https://gitcoin.co/explorer?q=cyber-search">
    <img src="https://gitcoin.co/funding/embed?repo=https://github.com/cybercongress/$repo_name$">
</a>
```
