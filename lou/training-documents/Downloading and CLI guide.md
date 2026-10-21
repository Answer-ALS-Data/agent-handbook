Document Title: Downloading and CLI Guide
Knowledge Base: KB 3: User Guides & Workflows
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: April 1, 2026
Version: 1.0

# Purpose

This document covers the end-to-end process for downloading data from the Neuromine Data Portal, including how to locate and install the download tool, authenticate and configure a destination, use both the GUI and CLI interfaces, understand download-related errors, and retrieve specific file types such as CSV clinical data and OMOP-standardized files. It also covers Mac-specific troubleshooting steps and what to do when downloads appear slow or stalled. This guide is intended as a training resource for Lou and should be referenced when users ask questions about downloading data, the CLI tool, download errors, file retrieval, or troubleshooting slow or failed transfers.

# Section 0: Small Data Downloads (No Download Tool Required)

*Users sometimes assume all data on the portal requires the Download Tool. SomaScan, NfL, and Metadata/Clinical Data packages are small files and are downloaded directly in the browser — no tool installation needed.*

Q: Do I need the Download Tool to download SomaScan, NfL, or Metadata data?

Context: Users ask how to download SomaScan, NfL, or clinical metadata and may expect the same Big Data workflow that applies to Genomics and Epigenomics.

A: No. SomaScan, NfL, and Metadata/Clinical Data are small files that download directly in your browser — no Download Tool is needed. After filtering your cohort and clicking "Download Data," you will see cards for each of these packages with direct download buttons:

- **Metadata and Clinical Data** — "Full Metadata" or "Filtered Metadata" buttons
- **Neurofilament Light Chain (NfL) Data** — "Full NfL Data" or "Filtered NfL Data" buttons
- **SomaScan Proteomics Data Package** — "Full SomaScan Data" button

The Download Tool is only required for **Big Data** packages (Genomics, Epigenomics, Transcriptomics, Proteomics, Methylation), which range from gigabytes to terabytes.

# Section 1: Finding and Installing the Download Tool

*Users frequently ask where to find the download tool and how to get started. The tool is not available as a standalone public download — it is accessed through the portal workflow after DUA approval. Multiple message log entries show users asking where the tool is or how to access it after selecting files.*

Q: Where do I find the download tool?

Context: Users often do not know the download tool is bundled into the portal workflow, and several message log entries show confusion about where to go after selecting data.

A: The download tool is accessed through the Neuromine Data Portal after your Data Use Agreement (DUA) has been approved and your account has been granted access. To access it:

1. Log into the Neuromine Data Portal and navigate to the Data Search page.
2. Use the search and filter tools to select the cohort and data types you need.
3. Click "Download Data" in the page footer.
4. On the Proceed Page, go to the Big Data section and choose the OMIC type and data level you need, then save your selection.
5. Open the download tool application and log in with your Answer ALS Data Portal credentials.
6. Select your saved result to begin the download workflow.

The download tool is available as both a GUI (graphical) application and a CLI (command-line interface).

---

Q: What operating systems does the download tool support?

Context: Users ask about compatibility, especially Mac users who have reported issues.

A: The download tool supports the following operating systems:
- Windows 10
- Mac OS
- Ubuntu 20.04 LTS
- Debian 10.4
- CentOS Linux 8

---

Q: Can I use the same login credentials for the download tool and the portal?

Context: Users sometimes think they need different credentials for the download tool and the portal.

A: Yes. You use the same credentials to sign in to both the Answer ALS Data Portal and the download tool.

---

# Section 2: Configuring Your Download Destination

*Before starting a download, users must define where files will be saved. The tool supports local storage, network storage, and Azure Blob storage as destinations.*

Q: How do I set up a download destination?

Context: Users ask about where files go and whether they need cloud storage to use the tool.

A: When you open the download tool and select your saved result, you will be prompted to define a download destination. You have three options:

1. **Local storage**: A folder on your own computer.
2. **Network storage**: A shared drive or network location.
3. **Azure Blob storage**: Enter your Azure Blob storage URL to download directly to the cloud. You must have your own Azure subscription — the Neuromine portal does not provide Azure storage.

Once your destination is set, the tool saves files there each time you download. It also inspects the destination folder for previously downloaded files and skips them automatically, saving storage space and time.

---

# Section 3: GUI Usage

*The GUI (graphical user interface) download tool walks users through the download process step-by-step. A tutorial video for the GUI download tool is available in the Learning Center on the Neuromine portal.*

Q: How do I download data using the GUI?

Context: A full walkthrough is the most frequently requested type of help in the message log for download-related questions.

A: To download data using the GUI:

1. Log into the Neuromine Data Portal and navigate to the Data Search page.
2. Use the search and filter tools to select the cohort and data types you need.
3. In the page footer, click "Download Data."
4. On the Proceed Page, go to the Big Data section and choose the OMIC type and data level you need.
5. Save your selection.
6. Open the download tool application and log in with your portal credentials.
7. Define your download destination (local folder, network location, or Azure Blob URL).
8. Select the saved result you want to download.
9. Review the download queue. Each package represents files for a specific OMIC type and data level. You can reorder the queue or skip any data types or levels you do not need.
10. Click Start to begin the download. The tool will show your progress.
11. To stop at any time, use the Stop option.
12. If any errors occur, check the Issue Log within the tool for details.

---

Q: Can I skip certain data types or levels in my download queue?

Context: Users who saved a large selection sometimes want to download only a subset of what they selected.

A: Yes. Once the download queue loads, you can review each package — each package corresponds to one OMIC type and data level — and skip any you do not want. You can also reorder items in the queue. The tool will automatically skip files already present in your destination folder.

---

# Section 4: CLI Usage

*The CLI (command-line interface) version of the download tool allows users to download data directly to a local server or integrate downloads into scripts. Several message log entries are direct bot failures on CLI questions — this section addresses those gaps explicitly.*

Q: How do I use the CLI version of the download tool?

Context: Direct bot failure. Users asked "How can I use the CLI version of the download tool?" and "How would I run the Neuromine CLI?" and received "I couldn't find specific instructions" responses. The CLI tool is the same download application as the GUI, accessed via command line.

A: The CLI download tool lets you download data from the command line, which is useful for server-based workflows or scripting.

To get started:
1. Log into the Neuromine Data Portal and navigate to the Data Search page.
2. Select your data, click "Download Data," and save your selection as described in the GUI workflow above.
3. Access the CLI download tool from the Neuromine Data Portal. Navigate to Datasets, select your dataset of interest, click the "NEXT" button, then click "Download Data." Under the "How to download Big Data?" section, you will see download buttons for Windows, MacOS, and Linux — select the one matching your operating system.
4. Authenticate using your Answer ALS Data Portal credentials.
5. Specify your download destination and the saved result you want to retrieve.

A step-by-step tutorial video for the CLI download tool is available in the Learning Center on the Neuromine portal (navigate to Learning Center → CLI Data Download Tool).

For additional help, contact data@answerals.org.

---

Q: Is there a direct link to download the CLI tool?

Context: Direct bot failure. A user asked "Can you give me a direct link to CLI data download tool?" and received "I couldn't find a direct link." The CLI tool is accessed through the portal, not a standalone public link.

A: The CLI download tool is accessed through the Neuromine Data Portal. Navigate to Datasets, select your dataset of interest, click the "NEXT" button, then click "Download Data." Under the "How to download Big Data?" section you will find download buttons for Windows, MacOS, and Linux. Select the one matching your operating system to download the tool.

If you need help, contact data@answerals.org.

---

Q: Is there a Python package or scripting API for automating downloads?

Context: A user asked "is there a python package? is there documentation so i can write a script to use it to download data?" The bot has previously hallucinated package names (e.g., "pip install neuromine-download" or "neuromine") and fictional REST API endpoints with fictional access tokens in account settings — none of these exist. Lou must not invent any of these.

A: No. There is no Python package and no REST API for the Neuromine download tool. There is no `neuromine` package, no `neuromine-download` package, no `pip install` command, no API endpoint, no access-token UI, and no developer/API documentation page in your account settings — none of these exist. Do not look for or attempt to install any such package; it does not exist.

The only supported method for command-line / scripted workflows is the **CLI download tool**, which is a desktop binary you download from the Neuromine portal (Datasets → select dataset → NEXT → Download Data → "How to download Big Data?" section → Windows / MacOS / Linux download buttons). The CLI tool can be invoked from a shell script for automation, but it is not a Python library and does not expose a REST API.

For questions about automating downloads with the CLI tool, contact data@answerals.org.

Note: Do not invent Python package names, pip commands, REST endpoints, API keys, or any other programmatic API for the download tool. The correct answer is always: no Python package or REST API exists; use the CLI download tool.

---

# Section 5: Download Errors

*Users encounter several types of download errors. This section covers billing errors, download limit messages, VPN-related timeouts, and blank screen issues in the tool.*

Q: I'm seeing a billing error when trying to download my saved cohort. What does this mean?

Context: Addressed in the portal FAQs. This error occurs when a saved cohort or search result points to a file path that has since been moved or updated on the portal.

A: This error typically occurs when a file in your saved cohort or data search has been moved or updated since you originally saved the result. As the Neuromine portal is continuously maintained, files may occasionally be relocated, causing previously saved results to point to outdated paths and triggering a billing or download error.

To resolve it:
1. Re-run your original data search or cohort filter using the same criteria.
2. Save the new version of the result.
3. Proceed with your download as usual.

If the issue persists, contact data@answerals.org.

---

Q: I got a "download limit exceeded" message. What does this mean and what should I do?

Context: Direct bot failure. A user asked "I was told download limit exceeded, what did it mean?" and received a generic fair-use explanation with no actionable guidance.

A: Download limits are associated with your account. When you exceed the threshold for your account, the system will block further downloads. To resolve it, contact data@answerals.org with details about what you were trying to download and the team will help you.

---

Q: My download timed out or failed to complete. What should I do?

Context: Addressed in the portal FAQs. VPN interference is the most commonly documented cause of download timeouts.

A: Download timeouts are often caused by a VPN or an unstable internet connection. VPNs can interfere with large file transfers or secure download sessions and may cause unexpected timeouts.

Recommended steps:
1. Disable your VPN (if you are using one) and try the download again.
2. Ensure your internet connection is stable.
3. If the issue persists, send your **log files** to data@answerals.org. Log files help the team diagnose the problem more quickly and accurately.

Note: Log files can be found in the Issue Log within the download tool.

---

Q: The download tool is showing a blank screen when I open it. What should I do?

Context: From the message log — a user reported a blank screen on launch. The bot initially suggested browser compatibility steps, but the download tool is a desktop application, not a browser.

A: The download tool is a desktop application, not a browser-based tool. If it is showing a blank screen:
1. Close the application completely and reopen it.
2. Check that you are running the latest version of the tool and update if needed.
3. Uninstall and reinstall the tool from the Neuromine Data Portal.
4. Verify your operating system is supported: Windows 10, Mac OS, Ubuntu 20.04 LTS, Debian 10.4, or CentOS Linux 8.
5. If the problem persists, contact data@answerals.org.

---

# Section 6: How Filters Affect Downloads

*Users select data using the portal's search and filter tools before downloading. Understanding how those filter choices determine the contents of the download package is important.*

Q: How do my search filters affect what gets downloaded?

Context: Users sometimes do not understand the connection between the portal's filter selections and the download package that appears in the tool.

A: Your download package is determined by the cohort and data selections you saved on the portal. The workflow is:

1. You use the search and filter tools on the Data Search page to identify participants and data types of interest.
2. On the Proceed Page, you choose the OMIC type and data level in the Big Data section and save the result.
3. That saved result defines what appears in your download queue in the download tool. Each package in the queue corresponds to one OMIC type and data level combination for the filtered cohort.
4. Within the tool, you can further narrow the download by skipping specific packages.

Clinical (CSV) data files are included in the download package regardless of OMIC filter selections.

---

Q: Can I update my filters and re-download?

Context: Users may want to adjust their cohort selection and download additional data after the initial transfer.

A: Yes. Run a new search with updated filters, save the new result, and select it in the download tool. The tool will skip files already present in your destination folder, so only new or changed files will be transferred.

---

# Section 7: CSV and OMOP File Retrieval

*The download package contains clinical CSV files and a standardized OMOP data folder. This section explains what each contains and how to find them.*

Q: What CSV files are included in the download package?

Context: Users ask what clinical data files they will receive when they download.

A: The Answer ALS download package includes the following CSV files:

- **aals_dataportal_datatable.csv**: High-level summary information keyed by participant ID, including demographics, cell line QC, and availability.
- **aals_participants.csv**: List of participants by ID indicating cohort group.
- **aals_released_files.csv**: List of all released files with data path and size.
- **Clinical_Dictionary_Oct_2025.csv** (or current version): Data dictionary containing all variables in the full clinical data, their possible values, and meanings.
- **Clinical folder**: Contains 33 CSV files with de-identified clinical measurements from participant visits, covering assessments such as ALSFRS-R, demographics, vital signs, medications, and more.
- **external_controls.csv**: Table with external controls with sex and age.
- **Sample_Mapping_File_Oct_2025.csv**: IDs for participant, sample, and cell-line with corresponding batch and shipment information.

For ALS TDI data, equivalent files are named with the `alstdiarc_` prefix.

---

Q: What are the OMOP files and where are they in the download package?

Context: From the message log, at least one user asked specifically about OMOP files and whether they are available in CSV format.

A: Yes, the OMOP files are provided in CSV format. The Answer ALS clinical data has been standardized to the OMOP Common Data Model (CDM) version 5.4. The standardized OMOP files are located in the **clinical_data_package/standardized_omop_data** folder of the download package, and include:

- **person.csv**: Unique participant identifiers and demographic information.
- **condition_occurrence.csv**: Disease and medical condition records.
- **measurement.csv**: Records from standardized examinations and testing.
- **observation.csv**: Clinical facts from examinations, questioning, and procedures.
- **drug_exposure.csv**: Medication and drug exposure records.
- **death.csv**: Date and cause of death records.
- **procedure_occurrence.csv**: Healthcare provider procedure records.
- **observation_period.csv**: Time span of each participant's records.
- **care_site.csv**: Differentiates between data from different sources (e.g., Answer ALS vs. ALS TDI).
- **concept.csv**: Custom concepts not in the official OMOP vocabulary, including ALS-specific terms.

The OMOP-standardized data is useful for combined analyses with other OMOP-based datasets such as ALS TDI. For the OMOP readme and ETL scripts, see the Answer ALS GitHub standardized-omop repository.

---

# Section 8: Mac Troubleshooting and Sync Delays

*Mac users have reported download issues. Several message log entries show the bot providing generic troubleshooting (check internet, check firewall) instead of tool-specific guidance. The most important Mac-specific facts: closing the app stops all progress, and there is no daemon mode.*

Q: I'm having trouble downloading data on a Mac. What should I check?

Context: Direct bot failure. A user reported trouble downloading transcriptomics level 4 on Mac and received generic suggestions (check internet, update tool, check firewall) instead of tool-specific guidance.

A: The download tool is supported on Mac OS. Here are the most important Mac-specific things to know:

1. **Closing the app stops your download. Closing the laptop lid (sleep) also stops the download.** The download tool does not run in the background — daemon mode is not supported. If you close the application, put the laptop to sleep, shut it down, or otherwise interrupt the active foreground session, your download will stop. Keep the app open and the laptop awake and connected to power for the full duration of the transfer. Workarounds like `caffeinate`, third-party "stay-awake" utilities, or disabling Energy Saver / sleep settings do **not** change this — the tool itself does not have a background/daemon mode and cannot continue a transfer once the foreground session ends or the network is interrupted.
2. **To resume a download**: Reopen the tool, log in, select your saved result and destination, and restart. The tool will skip files already downloaded and resume from where it left off — resume is supported on a per-file basis.
3. **Check Activity Monitor**: If the download tool appears stuck, open Activity Monitor (Applications → Utilities → Activity Monitor), find the tool in the process list, and verify it is running. If needed, select it and click the X button to force-quit, then reopen.
4. **Disable your VPN**: VPN connections can cause timeouts during large file transfers. Try disabling your VPN and restarting the download.
5. **Check the Issue Log**: If errors occur, check the Issue Log within the tool for details about what failed.
6. **Contact support with log files**: If the issue persists, send your log files to data@answerals.org. Generic troubleshooting (checking internet speed, firewall settings) is unlikely to resolve tool-specific errors — log files are much more useful for the team to diagnose the problem.

Note: Do not tell users that the download will keep running if they prevent sleep or use `caffeinate` — it will not. The correct guidance for "I need to close my laptop / go home" is: pause and resume the download later. The tool resumes at the per-file level.

---

Q: The download is taking a very long time to synchronize. What's happening?

Context: From the message log — a user reported the tool "taking forever to synchronize" even for a single CSV file. The bot gave generic internet-stability tips. The actual explanation is documented in the tool's feature notes: before transferring, the tool scans the destination folder for previously downloaded files.

A: Before beginning any transfer, the download tool scans your destination folder to identify files already present and skip re-downloading them. If your destination folder is large or contains many previously downloaded files, this initial scan can take significant time — even when you are only downloading a small new file.

If the scan seems excessive:
1. Wait for it to complete — this is expected behavior, especially for large destination folders.
2. If the tool appears frozen (not just slow), close it and reopen it. File-level resume means you will not lose completed downloads.
3. Ensure your destination storage (local or network) is accessible and responsive.
4. If the problem continues, contact data@answerals.org.

---

Q: How do I make sure the download tool is not running in the background on a Mac?

Context: From the message log — a user asked this as a follow-up during a troubleshooting session.

A: Open Activity Monitor (Applications → Utilities → Activity Monitor), find the download tool in the process list, select it, and click the X button in the top-left corner to quit it. Note that the tool does not support daemon mode and will not actively run itself in the background — but it may remain as an open process if not properly closed.

---

# General Support Reference

For any download or CLI issues not covered in this document, or for issues that cannot be resolved through the steps described above, contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
