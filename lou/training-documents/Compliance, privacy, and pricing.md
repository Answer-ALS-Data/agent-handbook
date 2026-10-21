Document Title: Compliance, Privacy, and Pricing
Knowledge Base: KB 1: Portal & Program Information
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: March 30, 2026
Version: 1.0

# Purpose

This document provides answers to frequently asked questions about the regulatory and privacy framework behind the data on the Neuromine Data Portal, what de-identification means in this context, how participant privacy is protected, and whether access costs anything. This guide is intended for use as a training resource for an LLM-based conversational assistant and should be referenced when users ask questions about data privacy, de-identification, HIPAA, compliance, data sharing restrictions, or pricing.

This document does not cover: the operational DUA process, eligibility rules, collaborator management, or specific data sharing prohibitions (see Access and Approvals Handbook); login and account issues (see Account and Identity FAQ); or portal navigation (see Portal Map and Naming Guide).

# Overview

All data on the Neuromine Data Portal is de-identified in accordance with HIPAA standards before it is made available to researchers. Access is governed by a Data Use Agreement (DUA) reviewed and approved by the Data Access Committee (DAC), which serves as the governance gate for responsible data sharing. The portal's data sharing framework has been approved under an institutional IRB. Registration, browsing, and data download are free for all users. There are no fees, subscriptions, or paid tiers.

# Section 1: De-identification and Data Privacy

*Users ask what de-identification means, how participant privacy is protected, and whether the data is truly anonymous. These questions often come from researchers who need to satisfy their own IRB or institutional review processes. The chatbot has previously given only surface-level answers to these questions, stating that "personal identifiers have been removed" without explaining what that means concretely.*

Q: Is the data on the Neuromine Data Portal de-identified?

Context: *This is a foundational question that comes up early in many user interactions. Users want confirmation that the data does not contain personally identifiable information. Some users phrase this as "is the data anonymized?" or "is the data safe to use?" The previous chatbot confirmed de-identification but did not explain the standard or process behind it.*

A: Yes. All data on the Neuromine Data Portal is de-identified in accordance with HIPAA standards before it is made available to researchers. This applies to both the Answer ALS and ALS TDI datasets. The datasets were de-identified by their respective source biorepositories before the data reached the portal. Participants are identified only by coded identifiers (GUIDs), not by names, dates, or any other personal information.

---

Q: What does HIPAA de-identification mean in this context?

Context: *Users — particularly those preparing IRB submissions or institutional data governance reviews — need to understand what de-identification actually involves, not just that it was done. The previous chatbot gave a generic answer ("personal identifiers have been removed") without explaining the process or the standard. Users need enough detail to satisfy their own compliance processes.*

A: HIPAA de-identification means that direct identifiers have been removed from the data before it is made available. Under the HIPAA Privacy Rule, de-identification requires that identifying information — including names, geographic data, dates (other than year), phone numbers, email addresses, Social Security numbers, medical record numbers, and other categories of identifiers — is removed or replaced so that the data cannot reasonably be used to identify an individual.

For the Answer ALS dataset, de-identification was performed by NeuroBANK at Massachusetts General Hospital (MGH) before the data was provided to the portal. For the ALS TDI dataset, de-identification was performed separately by ALS TDI before the data was provided. In both cases, participants are represented only by coded identifiers (GUIDs) in the portal.

The Neuromine team receives the data already de-identified. If you need specific details about the de-identification methodology used by the source biorepository for your IRB or institutional review, contact data@answerals.org and the team will help connect you with the appropriate information.

Note: *Do not claim a specific HIPAA de-identification method (Safe Harbor or Expert Determination). The portal team does not perform the de-identification and does not have documentation of the specific method used by the source biorepositories. If a user asks which method was used, direct them to support.*

---

Q: Does HIPAA apply to how I store or use the data?

Context: *Users sometimes ask Lou to decide whether their own storage or use of the data falls inside or outside HIPAA. That is a determination for the user and their institution, not for Lou.*

A: The data is de-identified in accordance with HIPAA standards before it is released. How you classify and protect the data on your own systems is up to you and your institution (for example your IRB or compliance office), and you remain responsible for handling it properly under your DUA. Lou does not decide whether your storage or use is HIPAA-compliant or outside HIPAA. For questions about the portal's de-identification, contact data@answerals.org.

---

Q: Do I need IRB approval to use the data from the Neuromine Data Portal?

Context: *Researchers frequently ask whether they need IRB approval before accessing or using the data. This question is especially common from users at academic institutions where all research involving human subjects data must go through an institutional review process. Some users assume that because the data is de-identified, they are automatically exempt from IRB review.*

A: The Neuromine Data Portal's data sharing framework has been approved under an institutional IRB, and the Data Access Committee (DAC) serves as the governance gate for responsible sharing. On the portal side, the compliance framework is in place.

Whether you need your own IRB approval to use the data depends on your institution's policies. Many institutions consider HIPAA de-identified data exempt from IRB review, but this determination is made by your institution, not by the portal. Consult your local IRB or institutional compliance office to confirm what is required before you begin your research.

Note: *Do not tell users they do or do not need IRB approval. The portal's own IRB and DAC framework is in place, but the user's institutional requirements are outside the portal's control. Always direct users to their own institution for this determination.*

---

Q: Does the portal comply with GDPR or other international privacy laws?

Context: *International researchers — particularly those in the EU — sometimes ask whether HIPAA de-identification is equivalent to GDPR anonymization, or whether the portal is GDPR-compliant. The previous chatbot could not answer this question at all. The portal operates under U.S. law and does not make claims about compliance with other jurisdictions' privacy frameworks.*

A: The Neuromine Data Portal operates under U.S. law, and the data is de-identified in accordance with HIPAA standards. The portal does not make claims about compliance with GDPR or other international privacy frameworks. The Data Use Agreement requires all users to comply with applicable laws in their jurisdiction.

If you are based outside the U.S. and need to determine whether the data meets your local regulatory requirements, consult your institution's data protection officer or legal team. For questions about the portal's de-identification standards or to request documentation for your institutional review, contact data@answerals.org.

Note: *Do not state that HIPAA de-identification is or is not equivalent to GDPR compliance. Do not make any claims about GDPR. If a user presses for a definitive answer, direct them to their own institution and to the support team.*

---

# Section 2: The Compliance Framework — Why Access Is Controlled

*Users sometimes ask why access requires a Data Use Agreement, why sharing is restricted, or why certain uses are prohibited. This section explains the regulatory and ethical reasoning behind the portal's access controls. For the specific rules, processes, and eligibility requirements, see the Access and Approvals Handbook.*

Q: Why does the portal require a Data Use Agreement?

Context: *New users sometimes view the DUA as a bureaucratic hurdle and want to understand why it is necessary. The DUA exists to protect participant privacy and ensure data is used for its intended purpose. Understanding the "why" helps users appreciate the importance of the process.*

A: The data on the Neuromine Data Portal originates from human research participants who consented to share their information for scientific research. The Data Use Agreement is the legal mechanism that ensures every user agrees to protect participant privacy, use the data only for approved research purposes, and comply with applicable regulations. It exists to honor the commitment made to the people who contributed their data.

The Data Access Committee (DAC) reviews all requests before access is granted. This governance structure ensures that data sharing is responsible, auditable, and consistent with the ethical obligations of the program.

For details on the DUA process, eligibility, and how to apply, see the Access and Approvals Handbook.

---

Q: Why can't I share the data with people who are not on my DUA?

Context: *Users sometimes want to share data files with colleagues who were not included in their original access request. The restriction exists for compliance reasons, not as an inconvenience. The Access and Approvals Handbook covers the operational rules and the process for adding collaborators; this entry explains the regulatory rationale.*

A: The DUA restricts data access to individuals listed in the approved Data Access Request. This restriction exists to maintain an auditable chain of custody and to ensure that everyone who handles the data has personally agreed to the same privacy and usage obligations. Allowing uncontrolled sharing would undermine the compliance framework and the commitments made to research participants.

If you need to add a new team member, the process is straightforward — contact data@answerals.org and the team will add them to your DUA. For details on how collaborator management works, see the Access and Approvals Handbook.

---

Q: Why is commercial use of the data restricted?

Context: *Users from industry or biotech settings sometimes ask why the DUA prohibits commercial use without prior written consent. This restriction is sometimes a concern for applicants from non-academic organizations who are unsure whether their intended use qualifies.*

A: The data on the Neuromine Data Portal was contributed by research participants for the purpose of advancing scientific research. The DUA restricts commercial use — including the development of commercial products or services — without prior written consent from the Answer ALS Foundation. This restriction protects participant intent and the research mission of the program.

If you have questions about whether your intended use qualifies as commercial, or if you would like to discuss a commercial use request, contact data@answerals.org.

---

# Section 3: Pricing and Access Costs

*Users ask whether portal access costs money, whether there are fees for specific services, and whether industry users face different pricing. The chatbot previously failed to answer pricing questions entirely — returning an empty response to "How much does access cost?" — and once incorrectly referenced a "system maintenance fee" that does not apply to the Neuromine Data Portal.*

Q: Does it cost anything to access and download data from the Neuromine Data Portal?

Context: *This is a critical gap in the previous chatbot's knowledge. A user asked "How much does access cost?" and received an empty response. Another user asked whether registration and download were free for non-commercial use and received a correct answer, but the response was not definitive enough. Users need a clear, unambiguous answer.*

A: No. Registration, browsing, and data download on the Neuromine Data Portal are completely free for all users — academic and non-academic. There are no fees, subscriptions, or paid tiers. This applies to all datasets hosted on the portal.

Note: *The previous chatbot once stated that "for-profit industry partners may incur a small system maintenance fee." This is not accurate for the Neuromine Data Portal. There are no fees of any kind. Do not reference maintenance fees or industry pricing in any response.*

---

Q: Are there any paid services or premium features on the portal?

Context: *Users sometimes ask whether there are paid tiers, API access fees, compute resource charges, or other premium features. This question came up in the conversation log when a user asked about paid items including API access, large downloads, and compute resources.*

A: No. There are no paid services, API fees, compute charges, or premium features on the Neuromine Data Portal. All portal features are available to all approved users at no cost.

---

Q: Are there download limits?

Context: *Users may encounter download limits and wonder whether this is a paywall or usage restriction. The portal limits downloads per research group as a practical infrastructure measure to manage data egress costs.*

A: The portal limits downloads per research group to manage data egress costs. This is not a paywall — all downloads are free. The expectation is that one member of each approved group downloads the data and places it on shared storage accessible to the entire team, rather than each team member downloading the full dataset individually. This approach reduces redundant downloads and keeps the platform sustainable.

If you have questions about download limits or need help coordinating data sharing within your team, contact data@answerals.org.

---

Q: Do biosamples or iPSC lines cost money?

Context: *Users sometimes ask about the cost of ordering iPSC lines or biosamples through the portal. The portal facilitates the ordering process, but pricing and fulfillment are handled by an external provider.*

A: Ordering iPSC lines and biosamples involves costs, but these are not set or managed by the Neuromine Data Portal. Pricing and fulfillment for biosamples and iPSC lines are handled by Cedars-Sinai. The portal provides information about ordering and links to the relevant resources, but all pricing, logistics, and payment are managed by Cedars-Sinai directly.

For details on how to order iPSC lines and what to expect, see the iPSC Lines and Biospecimen Access guide or contact data@answerals.org.

---

# General Support Reference

For any compliance, privacy, or pricing questions not covered in this document, or for issues that cannot be resolved through the information described above, users should contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
