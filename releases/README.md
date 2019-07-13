# Product pipeline

## Principles

1. Release perfection: quality control through publicly signed major releases;
2. [Project management](/project-management): one project = one repo = at least one owner. Every project has independent minor 0.x.0 or 0.0.x release pipeline,   like [chaingear](https://github.com/cybercongress/chaingear);
3. Product delivery: putting repositories together, can form a [product](https://github.com/orgs/cybercongress/projects) and its           [environment](https://github.com/topics/cyber-search).
4. Product releases, are major releases across all projects like x.0.0;
5. Transparency - every team member or external observer can track working process and see work progress.
6. Flexibility - there are only several obligatory rules of working processes (like attending sprint openings, closings), others can be dynamicly adjusted by team, if there is a need for it.
7. Interactivity - every team member can bring new ideas or change work process in case it will increase productivity.
8. Communications - continious cammunications between team members, short daily meetings for task actualising, groomings.
9. Working cycle - sprint (dutarion ~ 12 days) with opening and closing procedures.
10. Task division - project division to medium size tasks (GitHub epics) and small taskt (GitHub issues).
11. Planning - using GitHub project for placing epics in timeline.

## Tools

1. Github - development, task managment, work documents storage.
2. ZenHub app with browser extension - for enchancing GitHub task managment system.
3. Google Calendar - for event managment.

## Roles

- Product. Owner of repository.
- Agile master. Scrum master, process manager.
- Analyst. Requirement manager, technical writer.
- Engineer. Usually fullstack developer
- Designer. UX, graphic designer.

## Sprint structure

Sprint -  2 - week working cycle.

First week

|              Mon|            Tue|            Wed|            Thu|            Fri|   Sat |    Sun |
|-----------------|:-------------:|:-------------:|:-------------:|:-------------:|:-----:|-------:|
|11:00 Planning 2h|               |               |               |               |Day off|Day off||
|                 |               |               |               |               |       |       ||

Second week

|             Mon|            Tue|           Wed |            Thu|            Fri|    Sat|     Sun|
|-----------------|:-------------:|:-------------:|:-------------:|:-------------:|:-----:|-------:|
|                 |               |               |               |15:00 Demo 1.5h|Day off|Day off||
|                 |               |               |               |17:00 Retro 30m|       |       ||

### Obligatory events:

- Planning
- Demo
- Retrospective

### Optional events:

- Daily meetings
- Groomings

## Tasks

Tasks are presented in such ways:

Project/Release - big strategical type of work. It can take several month to be done.
Epics - part of project scope, massive task with subtasks or user stories. Epics can exist during one or several sprints.
Issue - subtask of epic or independent task. Issue should be closed in one sprint.

## Zenhub board pipelines:

1. New issues. All issues for before planning.
2. Icebox. Issues taken after planning that won't be done for current and next sprints.
3. Next spring. Issues taken after planning that won't be done for current sprint but will be migrated to next.
4. Backlog. Issues for current sprint pefore planning.
5. In progress. Issues taken from backlog for solving.
6. Review/QA. Done issues which need the review of team members.
7. Closed. Totally done issues.

## Valuation & reporting

1. Personal metrics

- Story points (all, backlog,icebox,next sprint, in progress, review, closed)
- Productivity (closed points divide on all points)

2. Product metrics

- Story points (all, backlog,icebox,next sprint, in progress, review, closed)
- Productivity (closed points divide on all points)

3. Product metrics

- Sprint story points (all, closed)
- Productivity (closed points divide on all points)

4. Valuation report

- OOS data (balances, expenses)
