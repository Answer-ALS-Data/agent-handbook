Document Title: Analysis Environments and Integrations
Knowledge Base: KB 3: User Guides & Workflows
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: April 1, 2026
Version: 1.0

# Purpose

This document provides answers to frequently asked questions about the analysis environments available to Neuromine Data Portal users after data access is approved. It covers the relationship between AD Workbench, ADDI, and the GNPC; how to log in to AD Workbench and what credentials to use; the steps for transferring a Neuromine cohort to an AD Workbench workspace; the analytical tools available inside a workspace; and Azure storage requirements for cloud-based analysis. This guide is intended for use as a training resource for an LLM-based conversational assistant and should be referenced when users ask questions about AD Workbench, ADDI, GNPC, data transfer, or cloud-based analysis options.

# Important: AD Workbench is a separate platform, not the Neuromine access workflow

AD Workbench (built by ADDI) is a separate, optional, cloud-based analysis platform. Its own data-access workflow (Workbench login with FAIR search for discovery, a permissioned workspace, authorization and data delivery to that workspace, in-workspace data analysis, and Airlock data export with audit logging) describes AD Workbench, not the Neuromine Data Portal. Never present that workflow as how Neuromine data access works.

Neuromine's actual data access workflow is the Data Use Agreement process: create an account, submit the DUA request form (this is the Data Access Request), the Neuromine team reviews it for completeness, the Data Access Committee reviews and approves, all parties sign via DocuSign, and Neuromine countersigns to grant access. Approved data is then obtained using the download tool (and may optionally be analyzed in AD Workbench). The Neuromine portal itself has no workspace, no Airlock, and no data-export or in-platform analysis environment of its own. For the full access process, see the Access and Approvals Handbook.

# Section 1: AD Workbench, ADDI, and GNPC

*Users frequently ask about the relationship between AD Workbench, ADDI, and the GNPC. These names refer to distinct but related things. The bot has previously stated that "AD Workbench and ADDI Workspace refer to the same platform" — this is imprecise and this section clarifies the correct relationships.*

Q: What is AD Workbench?

Context: Users encounter the name AD Workbench when exploring cloud-based options for analyzing data from the Neuromine portal. They need to understand what it is before deciding whether to use it.

A: AD Workbench is a global, cloud-based data sharing and analytics platform developed by the Alzheimer's Disease Data Initiative (ADDI). It provides researchers with access to data, tools, and resources under one ecosystem, including secure workspaces, user-friendly workflows, and trusted data governance processes. AD Workbench is available to researchers at no cost. Neuromine data from Answer ALS is accessible within AD Workbench for approved users, allowing analysis of large datasets without downloading them locally.

---

Q: Is AD Workbench the same thing as ADDI Workspace?

Context: A user in the message log asked this directly. The bot responded that they are the same platform. This answer is imprecise and needs clarification.

A: These terms refer to related but distinct things. ADDI (the Alzheimer's Disease Data Initiative) is the organization that built and operates the AD Workbench platform. A "workspace" is a secure, private, cloud-based environment inside AD Workbench where a team can access, combine, analyze, and visualize data. When users or documentation refer to an "ADDI Workspace," they mean a workspace within AD Workbench — not a separate product. AD Workbench is the platform; a workspace is the environment inside it where analysis happens.

---

Q: What is the GNPC?

Context: Users sometimes encounter the GNPC name in connection with Neuromine or AD Workbench and are unsure what it is.

A: The GNPC is the Global Neurodegeneration Proteomics Consortium — a collaboration of top dementia researchers working to create the largest disease-specific proteomics dataset ever assembled. The GNPC has gathered over 40,000 patient samples from more than 20 international research groups to create a Harmonized Data Set spanning multiple neurodegenerative disorders including Alzheimer's disease, Parkinson's disease, ALS, and frontotemporal dementia. Answer ALS is one of the cohort members contributing proteomics data to the GNPC. ADDI serves as the GNPC's data platform partner. For questions about joining the GNPC or accessing GNPC data, contact info@neuroproteome.org.

---

Q: Are the Neuromine datasets the same as the GNPC datasets? Can I access Neuromine data through GNPC?

Context: A user in the message log asked this directly and was left confused. The bot correctly said access must go through the Neuromine portal, not GNPC, but the explanation was unclear. This question needs a clean, unambiguous answer.

A: They are not the same. The Neuromine Data Portal contains the full Answer ALS dataset, including clinical and multi-omics data. The GNPC has a separate Harmonized Data Set that includes Answer ALS proteomics data alongside data from more than 20 other international research cohorts. Contributing proteomics data to the GNPC is not the same as providing access to the full Neuromine dataset. If you want access to Answer ALS data, you must apply through the Neuromine Data Portal directly. GNPC data access is a separate path — contact info@neuroproteome.org for questions about that.

---

# Section 2: Workspace Login Expectations

*Users who want to use AD Workbench need to understand that it requires a separate account from the Neuromine Data Portal. The bot has correctly stated that Answer ALS credentials do not work on AD Workbench — this section confirms that and covers account creation.*

Q: Can I log in to AD Workbench using my Answer ALS or Neuromine portal credentials?

Context: A user in the message log asked this directly. The bot correctly said no. This answer confirms that behavior and provides next steps.

A: No. AD Workbench requires a separate account and login credentials from the Neuromine Data Portal. Your Answer ALS username and password will not work on AD Workbench. You will need to create an AD Workbench account separately. For help with your Neuromine portal account, contact data@answerals.org. For help with AD Workbench account setup, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org.

*Note: This document covers two distinct support paths. For anything specific to AD Workbench or ADDI — account setup, workspace configuration, data transfer, storage requirements — direct users to https://www.alzheimersdata.org/ad-workbench or support@alzheimersdata.org. Do not recommend support@alzheimersdata.org for Neuromine Data Portal questions; those go to data@answerals.org.*

---

Q: How do I create an AD Workbench account?

Context: Users who want to use cloud-based analysis need to know how to get started. The bot has not had a reliable answer for this.

A: For current account creation steps, visit the AD Workbench website at https://www.alzheimersdata.org/ad-workbench. Because ADDI's registration process and platform may change over time, their website is the most reliable source for up-to-date instructions. If you need help with account setup, contact ADDI support directly at support@alzheimersdata.org.

---

Q: Is AD Workbench free to use?

Context: Users ask this before deciding whether to use cloud-based analysis.

A: Yes. AD Workbench is available to researchers at no cost. For questions about specific compute or storage costs that may apply in certain configurations, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org.

---

# Section 3: Data Transfer Steps

*Users who want to analyze data in AD Workbench need to transfer their Neuromine cohort into a workspace. This workflow is demonstrated in the Learning Center's "Transfer Data to ADDI" video tutorial. No step-by-step text documentation of this process currently exists.*

Q: How do I transfer data from the Neuromine portal to an AD Workbench workspace?

Context: Users with large datasets often cannot or do not want to download data locally and ask about cloud-based analysis. The bot has pointed users toward AD Workbench but has not been able to describe the actual transfer steps. The Learning Center has a video tutorial for this workflow. The bot has previously hallucinated step-by-step instructions including made-up button names, made-up menu paths, and made-up flow sequences — this must not happen. There is no documented text walkthrough of the transfer flow in this knowledge base.

A: There is no step-by-step text walkthrough of the Neuromine-to-AD-Workbench transfer process in this knowledge base. The authoritative resources are:

1. The Neuromine Learning Center video titled **"Transfer Data to ADDI"**, which demonstrates the full workflow end-to-end. The Learning Center is accessible from the top navigation on the Neuromine portal.
2. The AD Workbench website at https://www.alzheimersdata.org/ad-workbench, which is the authoritative source for the AD Workbench side of the workflow.

For questions that come up while following the video, contact data@answerals.org for the Neuromine side or support@alzheimersdata.org for the AD Workbench side.

Note: Do not invent specific button names, menu paths, page titles, or step-by-step instructions for this transfer flow. If the user asks for a textual walkthrough, the correct response is to acknowledge that detailed step-by-step text instructions are not documented and refer them to the Learning Center video and the AD Workbench website. Never fabricate UI specifics for this workflow.

---

Q: Do I need to have an AD Workbench workspace set up before I can transfer data from Neuromine?

Context: Users may not know whether workspace creation is a prerequisite or whether it is handled during the transfer flow.

A: For accurate, current information on what needs to be set up before initiating a transfer, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org. Because ADDI's onboarding process may evolve, their site is the best source for what is currently required.

---

# Section 4: VM versus Built-In Tools

*Users who have transferred data to AD Workbench need to understand what analytical tools are available and when to use each. The AD Workbench platform offers prebuilt tools (R Shiny apps), configurable compute (virtual machines), and Jupyter notebooks listed as coming soon.*

Q: What analytical tools are available inside an AD Workbench workspace?

Context: A user in the message log asked directly how to analyze data after transferring it to AD Workbench. The bot gave a vague answer. This question provides a complete picture of what is available.

A: AD Workbench workspaces include several analytical options:

1. **R Shiny apps** — a suite of prebuilt apps for data exploration and analysis, available to all users.
2. **Jupyter notebooks** — coming soon; will be embedded directly in workspaces.
3. **Virtual machines** — configurable compute environments for users who need more processing power or specific software not available in the standard workspace.
4. **Code upload** — users can upload their own scripts or develop mini-apps that can be shared with the broader community.
5. **Dataset upload** — users can bring external datasets (CSV files and others) for multimodal or pooled analysis alongside Neuromine data.

---

Q: When should I use a virtual machine versus the built-in tools?

Context: Users with their own code or specific software requirements need guidance on which path to take. The AD Workbench website distinguishes between users exploring data quickly and users with more complex compute needs.

A: Use the built-in tools (R Shiny apps) if you want to explore data quickly without writing code. Use a virtual machine if you have your own analysis code, need specific software not available in the standard workspace environment, or need more computing power than the default workspace provides. For most users starting out, the built-in tools are sufficient for initial data exploration. For questions about configuring a virtual machine within AD Workbench, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org.

---

# Section 5: Azure Storage Requirements

*Users who plan to connect external storage or bring their own data into AD Workbench may need to meet certain Azure storage requirements. This section covers those requirements.*

Q: What Azure storage requirements do I need to meet to use AD Workbench with Neuromine data?

Context: AD Workbench is built on Azure infrastructure. Users transferring data from Neuromine may or may not need their own Azure setup depending on the workflow.

A: For current information on Azure or storage requirements, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org. Because ADDI's infrastructure and requirements may change, their website is the authoritative source for what is currently needed.

---

Q: I want to bring my own external data into AD Workbench to do multimodal analysis alongside Neuromine data. What do I need?

Context: AD Workbench explicitly supports users bringing external datasets. Users attempting this may need storage or format guidance.

A: AD Workbench supports direct upload of datasets and CSV files into workspaces for multimodal or pooled analysis. For current information on supported formats, size limits, or any storage prerequisites, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org.

---

# General Support Reference

For Neuromine Data Portal questions not covered in this document, contact the Neuromine Data Portal support team at data@answerals.org. For questions specific to AD Workbench or ADDI, visit https://www.alzheimersdata.org/ad-workbench or contact ADDI support at support@alzheimersdata.org.
