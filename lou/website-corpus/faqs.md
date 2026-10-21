---
title: "Faqs"
url: https://dataportal.answerals.org/faqs-2
slug: faqs
scraped_at: 2026-04-15T18:28:15Z
content_hash: fb7591482d582cb6
source: dataportal.answerals.org
---

# Faqs

Categories

##### Below are some common questions regarding Answer ALS data and data access process. If you don’t find your question below feel free to reach out to us.

#### Data Access and Download

How do I register for access to the Answer ALS data?

To register for access to the Answer ALS data, you will need to create an account on the Answer ALS data portal and submit a Data Use Agreement (DUA). Once your data access request has been approved by our Data Access Committee (DAC), you will be granted access to the full Answer ALS dataset and tool suit.

Can you explain the purpose of signing a Data Use Agreement and the process for doing so?

A Data Use Agreement (DUA) is a legally binding document that outlines the terms and conditions of using the data. The DUA ensures that the data will be used for research purposes only and that the data will be protected according to the standards set by the data provider (Answer ALS).
The process for signing a DUA involves creating an account on the data portal, reading/agreeing to the terms of a Data Use Agreement, signing the DUA, and submitting the completed DUA for review. You can download a PDF version to review before proceeding to the “Request Data Access” process.

[Answer ALS DUA]((document on the portal))

What guidelines can you provide for who should sign the DUA?

If you are a graduate student, postdoc, scientist, or research associate, you must have your supervising PI, Director, or above co-sign the DUA. Please include the title and level of this person in your request using the Collaborator section. If you are a Principal Investigator (PI), Director, or above, you may be the Data Requestor and do not need to list another PI or Director as a collaborator.

A Business Official also needs to sign on behalf of your associated entity, so please check with your contracts office or PI to ensure the correct person is identified for this role. If you have collaborators outside of your institution, they must request separate access. However, if they are part of your institution, they may be added as a collaborator on this request.

How do I download data from the site?

Once your DUA has been approved, and your account has been granted access to the data, you can download data from the site by logging into your account and navigating to the “Data Search” page. You can select the cohort and data of interest and begin the download process.  Please note that you will need to download the “Download Tool” from the site in order to begin data transfer. You have the option to use a user-friendly GUI or CLI interface.

In what format are the Clinical and OMIC data files provided?

The Clinical data files are provided as CSV files (.csv).
Data Dictionary for OMIC data can be found here [OMIC Data Dictionary]((document on the portal)).

Is it possible to make changes to the Data Use Agreement to align with my organization's legal requirements?

No. Answer ALS will not accept modifications to the Data Use Agreement under any circumstances.

How long should I expect the data access process to take after submitting a Data Use Agreement?

The data access process can take a few days up to several months, depending on the complexity of the DUA and the number of requests currently being processed. Getting the right people at your institution involved early helps to make the process move faster.

Are there any restrictions on how the data can be used?

Rules and regulations regarding the the Answer ALS data usage can be found in the Data Use Agreement (Answer ALS DUA).

[Answer ALS DUA]((document on the portal))

What is the difference between Open Source and Open Access to data?

The main difference between open-source code and open access to human subject data is the nature of the information being shared and the ethical considerations involved. Open-source code refers to software whose source code is made available to the public, without any restrictions, enabling anyone to view, modify, and distribute the code. On the other hand, open access to human subject data involves making data from research studies available to the public, but with additional ethical considerations, such as obtaining informed consent from study participants and ensuring their privacy and confidentiality are protected. This typically involves signing a data use agreement, which outlines the terms and conditions for accessing and using the data, including data security and confidentiality, and other governance measures such as institutional review board (IRB) approval, data sharing policies, and data management plans.

Why am I seeing a billing error when trying to download my saved cohort data?

This error may occur if a file in your saved cohort or data search has been moved or updated since you originally saved the result. As the Neuromine portal is continuously maintained and improved, files may occasionally be relocated to optimize storage or access. When this happens, previously saved search results may point to outdated file paths, triggering a billing or download error.

To resolve the issue:

1. Re-run your original **data search or cohort filter** using the same criteria.
2. Save the **new version** of the result.
3. Proceed with your download or transfer request as usual.

This will ensure your results are linked to the current file locations and can be accessed without error.

If the issue persists, feel free to contact support for assistance.

What should I do if the system times out during data download?

If your download times out or fails to complete, this is often due to a **VPN connection or an unstable internet connection** on the user’s end. VPNs can interfere with large file transfers or secure download sessions and may cause unexpected timeouts.

**Recommended Steps:**

1. **Disable your VPN** (if you’re using one) and try the download again.
2. Ensure your internet connection is stable and not experiencing interruptions.
3. If the issue persists, please send your **log files** to [data@answerals.org](mailto:data@answerals.org) so our team can help troubleshoot the problem.

The log files will help us better understand what’s happening on your system and provide faster, more accurate support.

We’re here to help—don’t hesitate to reach out!

#### OMICS Data

What types of OMICs data does Answer ALS have available?

Answer ALS has various types of OMICs data available, including genomics, transcriptomics, proteomics, and epigenomics. For a description of data types and levels, please refer to the OMIC Data Dictionary.

[OMIC Data Dictionary]((document on the portal))

How often are the OMICs dataset updated via releases?

OMIC data is planned for release every 6 months however, due to the nature of data generation and curation, this frequency of OMICs releases is not guaranteed. Answer ALS periodically releases our OMIC data as it is generated for our organization.

How many participants are included in the OMICs data?

The number of participants’ data available for each OMIC type evolves between releases as data is processed. At the end of the project, we expect approximately 1269 participants, both subjects and controls, to have an OMIC data set available. This number is not guaranteed and is based on the production of cell lines and OMIC data.

How is the OMICs data collected and processed?

Please refer to the Assays and Pipelines section on the DATA INFORMATION  page for sample and data processing details.

Why is the line CTRL-NEUEU392AE8 present in the data multiple times?

The CTRL-NEUEU392AE8 is used as a technical and differentiation batch control. Please refer to the Experimental design section on the ABOUT page for more information.

Are the data generated from a single sample or multiple samples per participant?

All data is generated from motor neuron lines derived from each participant’s iPS cell line. Each motor neuron line is collected, and aliquots are sent to each OMIC center for processing and data generation.

Are there any limitations or known biases in the OMICs data?

One of the dominating contributors to the gene expression changes observed in our initial principal component (PCA) analysis is the inherent sex effect. Genes that contribute to the sex effect include both sex chromosome linked genes and autosomal genes. This gender specific gene expression has also been reported in post mortem human brains, as well as IPSCs. In order to extract disease relevant signal, we recommend controlling sex effect for your downstream analysis. For example, excluding chrX, chrY linked genes and adding an additional binary variable to the design account for sex effect.

The standard step after obtaining level 3 data (Counts) is statistical inference of systematic changes between conditions (e.g ALS and CTR) by modeling gene expression data with a binary variable with two levels (design ~condition, condition =0 for CTR, 1 for ALS). In the presence of confounding factors a more complex design (e.g. design~batch + condition) may be needed to exact the disease relevant signal while controlling for the confounders.

#### Clinical Data

What types of clinical data are available?

The types of clinical data available through Answer ALS may include demographic information, medical history, symptoms, functional assessments, and other information relevant to the study of ALS.

How is the clinical data collected and organized?

The clinical data is collected through various methods such as patient interviews, medical records, and standardized assessments and organized in a way that allows for easy access and analysis. NeruoBANK manages and stores the full data set for the Answer ALS program.

To share the data, the data is curated to remove any potentially identifiable information before releasing it through the data portal.

How many participants' data are included in the clinical dataset?

As of release 5, there are 1041 participants included in the clinical dataset. There is also a
limited set of 228 external control participants. These participants will not be included in the clinical data files but will be on the data portal table and have a separate file with minimal information in the download package.

Are the Clinical data files accompanied by any documentation or variable description?

The Answer ALS clinical data dictionary provides all relevant information regarding field/value definitions, structure, and order.

[Answer ALS Clinical Data Dictionary]((document on the portal))

#### General Questions

What is the goal of the data sharing site?

The Answer ALS data-sharing site aims to accelerate the discovery of new treatments for ALS by providing researchers with access to high-quality, multi-OMIC data sets generated from individuals with ALS, as well as relevant clinical data. By making this data widely available, we aim to encourage collaboration among researchers and facilitate the identification of new therapeutic targets and biomarkers, ultimately leading to improved diagnosis, prognosis, and treatment of ALS. The data-sharing site also aims to increase transparency and reproducibility in ALS research and to promote data sharing as a best practice in the scientific community.

What is your IP (intellectual property) policy?

Achieving maximum public benefit is the ultimate goal of data distribution through the Answer ALS data repositories. The AALS Program believes that these data should be considered as pre-competitive and requests Approved Users not to make IP claims derived directly from the Answer ALS dataset(s). However, the AALS Program also recognizes the importance of the subsequent development of IP on downstream discoveries, especially in therapeutics, which will be necessary to support full investment in products to benefit the public. The AALS Program requests that the Requestor and all Approved Users acknowledge that they will not claim IP on any of the datasets made available through the data portal. However, it does support IP development based on derivative discoveries made from these data.

It is expected that these AALS-provided data, and conclusions derived from the data, will remain freely available without the requirement for licensing. The AALS Consortium encourages the broad use of Answer ALS datasets and a responsible approach to the management of intellectual property derived from downstream discoveries in a manner consistent with the NIH Best Practices.

How can I provide feedback or report any issues with the data or site?

To provide feedback or report any issues with the data or site, please contact Answer ALS by email at answeralsdata@gmail.com.

I recently ordered cell lines from the Cedars biorepository, how can I find out what data is available on those lines?

On the search page, once you are an approved user, you will navigate to the “Show filters” on the very left-hand side of the page and open using the symbol. This will open a set of filters that you can use to search. In the “UPLOAD CASE SET” window, you can use iPSC line names, GUIDs, or participant ID’s to find your specific set. Be sure to select the “Identifier Type” and name your case set before hitting submit.

How do I cite using Answer ALS data in my publications?

**ANSWER ALS Acknowledgement:**

“Data used in the preparation of this article were obtained from the ANSWER ALS Data Portal (AALS-01184). For up-to-date information on the study, visit https://dataportal.answerals.org.”

**CITE ANSWER ALS DESCRIPTION PAPER**

Baxi, E. G. *et al.* [Answer ALS, a large-scale resource for sporadic and familial ALS combining clinical and multi-omics data from induced pluripotent cell lines.](https://www.nature.com/articles/s41593-021-01006-0) *N*at Neurosci 1-12 (2022) doi:10.1038/s41593-021-01006-0.

**ANSWER ALS Cohort Acknowledgements:**

“Clinical data and biosamples used in the preparation of this article were obtained from the Answer ALS Foundation Program, ‘Answer ALS’. For up-to-date information on the program, visit https://www.answerals.org.
