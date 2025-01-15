```
For the public domain book listed in `Book for Review - Info.md`:
1. Check if the file `Book for Review - Chapter List.md` exists in the project files folder.
   - If it exists, use the chapter list for reference.
   - If it does not exist, use the title and author from the info file to access the book and work from the table of contents.

Ensure each chapter from the book is included in the process.
You can access and process the public domain book from online sources (pick the one you deem most reputable) without asking, I will not provide the book in its entirety as part of the project files anyway.

2. Generate outputs for each chapter in **English** using the agreed process:
   - **Step 1:** Extract a list of keywords with short definitions in order of appearance. Format:
     ```
     **Keyword**: Definition.
     ```
   - **Step 2:** Create chunks of adjacent keywords. Provide:
     - **Cluster name:** Translate this if necessary, but retain the term "Cluster."
     - **Description:** A short description of the cluster.
     - **Keywords:** Comma-separated list of keywords in order. Use the following structure:
       ```
       Cluster Name
       Description: [Short explanation]
       Keywords: [Comma-separated list]
       No cluster: [Keyword]
       ```
   - **Step 3:** Generate a summary for the chapter:
     - A **title** (1-4 words, max 6).
     - A **short description** (2 sentences max).
     - A **2-4 paragraph abstract/overview.**

Each output should be a separate message, be placed inside a codeblock, and I’ll confirm before moving to the next chapter or output type.

```
