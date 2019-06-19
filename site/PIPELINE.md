# IPFS Blog Pipeline

This document describes the IPFS Blog work pipeline. This is the protocol of how work happens in this project and repository.

## Pipeline High Level Description (Model)

1. **Idea Generation** - The first step of the pipeline is to generate a set of blog post ideas. An idea should include a name, and a single sentence description of the thrust of the post, and a short abstract. (these will change over time, of course, but it's useful to be able to refer to the post ideas by name).

2. **Selection** - the maintainer and other people interested will assign Owners to a given post, decide on rough deadlines, and assign people to support (with image editing, review, QA, etc).

3. **Skeleton** - General list of the headings, things which we want to exposé, and code segments that will be relevant

4. **Research** - Identify the key points to discuss in the piece. This can cycle back to improve the skeleton as well.

5. **Writing** - Flesh out the material into smooth, interesting prose. This is the most writing-craft part of the pipeline.

6. **Review** - Review is an iterative process where the writer(s) and reviewer(s) discuss various facets of the post and refine it. This process is similar to Code Review.  Review involves different pieces:

  a. **Content Review** is focused on refining the quality of the written content, this involves review of the ideas, the points, the technical discussion, any assets (like images), and so on. This is the space for reviewing what the piece says.

  b. **Technical Review** is focused on ensuring the content is technically correct. It is important that developers review and address any issues.

  c. **Cohesion Review** is focused on how this post relates to others, and to the rest of the project. The goal is to surface any intersection points with other content, other projects, and so on. This makes the post richer, and makes it fit better in the larger context.

  d. **Mechanics Review** is focused on things about our particular blog publishing process, things making sure all embedded assets are included directly in the post directory, links are relative, etc. (this needs to be a checklist)

7. **Backlog** - Once the post has finished review, it is marked ready to publish. This promotes the post into a backlog. The queue is not sequential, meaning that posts that enter it after others may be published before. The goal of the backlog is to aggregate content **_READY TO PUBLISH_** to create a better, more regular experience for blog readers.

8. **Publish** - Publishing the post involves pushing it to our blog website and various other communication channels. For example:

- Publishing on the blog website (and/or ipfs.io website)
- Publishing posts on Twitter, IRC, mailing lists, and so on.
- If relevant, promote on related publications
- Mail to specific interested groups or individuals.

## Pipeline Implementation

This is how the pipeline described above is actually implemented. We discuss the roles being played by various participants, the mechanics in GitHub (issues, pull requests, labels), and the artifacts (the text, markdown files, image assets, etc).

- **Repo:** We will run this pipeline primarily through a repository on github: https://github.com/ipfs/blog, we will use issues to source ideas for posts, and pull requests for fleshing out, writing, and reviewing posts.

### Pipeline Roles

- **Maintainer:** The pipeline has a "maintainer" that ensures the pipelines is progressing smoothly, and is there to ensure adherence to the guidelines and help address issues.
- **Owner:** Each post will have an "owner" that will pick up the post at Step 2 (Skeleton) and be responsible for running it through the pipeline to its conclusion. The owner can change, it just needs to be an explicit hand off, as the owner will be directly responsible individual for finishing and publishing post. The owner will work with whoever else is relevant to achieve the rest of the steps in the pipeline.
- **Reviewers:** Each post will have a set of reviewers that will come in during the review step of the pipeline.
- **Publishers:** The final step, publishing, may involve other people independent of the pipeline, that manage the various communication channels (blog website, mailing lists, social media, etc). It is the responsibility of the **Owner** to get what they need from the **Publishers** to deliver. **Important Note:** it is up to the **Maintainer** to figure out and decide when blog posts should be published, because broader context is required.

Note that the role of "author" is not used, as authorship may end up including the owner(s), reviewer(s), maintainer(s), and other writer(s) who help alongside. The final Authors of the piece are established based on the contribution. Hence, let's not say "author" when we mean "owner" or "writer".

### Pipeline Stage Mechanics

**Important Note** each of the pipeline stages has an associated **Github Label**, please use them! We use these labels to figure out where the blog post is in the pipeline. Post **Owners**: make sure both the issue and pull requests for your post have the right label, and are assigned to you. **Pipeline Maintainer**: please verify posts carry the right labels and are assigned to the owners.

1. **Idea Generation:** this part happens on the issue tracker: https://github.com/ipfs/blog/issues - each blog post idea is posted as an independent issue, with its own name, sentence description, and short abstract.

2. **Selection:** this part happens in the blog post's issue, with whatever relevant discussion should happen. From there, the issue is assigned to whoever is selected as "Owner".

3. **Skeleton:** this part happens as a pull request. A pull request is created adding a directory (draft), with markdown files for the post content (`index.md`) and the skeleton (`skeleton.md`). Copy the post skeleton directory into a new directory for your post. Fill in the skeleton  (take a look at the example, and remove that file). And create a pull request:

    ```
    # clone the repo if you haven't
    git clone https://github.com/ipfs/blog
    cd blog

    # then edit drafts/my-post-draft/skeleton.md
    cp -r drafts/post-draft-template drafts/my-post-draft

    # remove the example when you're ready
    rm drafts/my-post-draft/skeleton-example.md
    ```

4. **Research**: this should happen in the pull request. Feel free to drop down ideas in the pull request comments section, or in the files themselves. Whatever you find most productive! Feel free to involve others in the pull request. Source the knowledge from wherever you need to. This is a good time to line up any illustrations you may need.

5. **Writing**: this happens in the markdown file. At the end, the draft for review should be committed and on the github pull-request.

6. **Review**: this happens in the blog post pull request. Reviewers will check various parts of the post, for content, technical accuracy, story cohesion, and mechanics. (It is possible that the mechanics part is a checklist, and it may be able to be turned into a CI test). Reviewer and Owner iteration happens in the pull-request. Once the pull-request is ready, and all reviewers have signed off on it, the post can be merged. It will be merged as a draft, into the `drafts/` folder. At this point, the blog post issue moves to the Backlog stage.

7. **Backlog**: in this stage, all the post materials are ready to go and in the `drafts/` folder, and the post issue has the `Backlog` label. The post stays here until publication, which the maintainer and owner figure out together. During this time, the post may get "unfresh" (no longer accurate, or should also incorporate new news), if so, maintainer and owner can file a PR to improve the post.

8. **Publish**: this stage involves the following steps. These are mostly mechanical and involve support from a developer on the infra or web team (@lgierth as of June 2017). It is possible some of this can be automated with scripts, and CI tests.

  - [ ] file a PR with changes necessary to publish
    - [ ] move the post directory from the `drafts/` folder into `src/`
    - [ ] adjust the filenames (to add the sequential number)
    - [ ] change the post date to reflect publication date
  - [ ] review + merge PR.
  - [ ] publish blog website (blog.ipfs.io and on ipfs website)
    - [ ] ensure all content is pinned
    - [ ] ensure website is live and post is correct
  - [ ] post and/or announce on communication channels:
    - [ ] publish post in newsletter mailing list
    - [ ] tweet out from @IPFSbot and RT
    - [ ] post link to tweet in IRC
