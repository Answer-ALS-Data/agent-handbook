Document Title: Account and Identity FAQ
Knowledge Base: KB 1: Portal & Program Information
Category: User-Facing Guide
Platform: Neuromine Data Portal (Answer ALS)
Support Contact: data@answerals.org
Last Updated: March 06, 2026
Version: 1.0

# Purpose

This document provides answers to frequently asked questions about account management and identity on the Neuromine Data Portal. It covers login issues, account creation conflicts, profile changes, account deletion, and credential management. This guide is intended for use as a training resource for an LLM-based conversational assistant and should be referenced when users ask questions related to authentication, account setup, or identity management on the portal.

# Section 1: Login Errors and Verification Code Issues

*The Neuromine Data Portal supports four authentication methods: Local Registration (Neuromine), AD Data Initiative (ADDI), Microsoft, and Google. Each account is tied to exactly one authentication method — users must always sign in using the same method they used to register. When users sign in via local Neuromine registration, Microsoft Azure AD B2C sends an email-based verification code that must be entered to complete sign-in. Issues with this process are among the most commonly reported login problems. Users authenticating via Google, Microsoft, or ADDI follow those providers' respective sign-in flows and do not use B2C verification codes.*

Q: What authentication methods does the Neuromine Data Portal support?

Context: Users sometimes do not know which sign-in method they used to register, or are not aware that the portal supports multiple authentication paths.

A: The Neuromine Data Portal supports four authentication methods for registration and sign-in:

1. **Local Registration (Neuromine)**: The most commonly used method. Users create an account directly on the portal with an email address and password. Authentication is handled through Microsoft Azure AD B2C, which sends email-based verification codes as part of the sign-in process.
2. **AD Data Initiative (ADDI)**: Users with an existing ADDI account can use their ADDI credentials to sign in.
3. **Microsoft**: Users can sign in using their existing Microsoft account credentials.
4. **Google**: Users can sign in using their existing Google account credentials.

Each account is tied to exactly one authentication method. You must always sign in using the same method you used when you first registered. If you are unsure which method you used, contact data@answerals.org and the team can look up your account.

---

Q: I'm not receiving my verification code email. What should I do?

Context: When a user attempts to sign in via local Neuromine registration, Microsoft B2C sends a verification code to their registered email address. Some users report never receiving this code. This is a known issue that can occur due to email provider filtering, network delays, or temporary service disruptions on the B2C side.

A: First, check your spam or junk folder — verification code emails from Microsoft may be filtered automatically by your email provider. If the email is not in your spam folder, wait a few minutes and try requesting a new code, as there can sometimes be a delay in delivery. If you are still not receiving the verification code after multiple attempts, contact data@answerals.org for further assistance.

Note: Verification code delivery is managed by Microsoft's B2C authentication service and is outside the direct control of the Neuromine team.

---

Q: I'm trying to sign in but the system says I am not recognized. What does this mean?

Context: This error typically occurs when a user attempts to sign in using a different authentication method than the one they originally registered with — for example, a user who registered with Google sign-in then tries to log in through the local Neuromine sign-in form. Because each authentication method creates a separate identity, the local sign-in system does not recognize the Google-registered account.

A: Make sure you are signing in using the same authentication method you used when you first registered your account. The portal supports four sign-in methods: local Neuromine registration, ADDI, Microsoft, and Google. If you registered using Google, you must sign in with Google every time. If you registered using the local Neuromine form, you must use that form to sign in. If you cannot remember which method you used, contact data@answerals.org and the team can look up your account.

---

Q: I'm getting an internal server error when I try to sign in. What should I do?

Context: Internal server errors during sign-in can have multiple causes, including temporary service disruptions on the Neuromine side or with the Microsoft Azure AD B2C authentication provider. The exact cause is not always immediately clear from the user's perspective.

A: An internal server error during sign-in can be caused by a number of things, including temporary service disruptions on the portal or with the authentication provider. Please wait a few minutes and try signing in again. If the issue persists, contact data@answerals.org so the team can investigate.

---

Q: How do I change or reset my password for the portal?

Context: Users who registered with the local Neuromine email/password method can reset their own password using the "Forgot your password?" link on the sign-in page. Users who registered with Google, Microsoft, or ADDI do not have a Neuromine password and reset it through that provider instead.

A: If you registered with an email address and password (local Neuromine registration), you can reset your own password from the sign-in page: click the "Forgot your password?" link (next to the email/password fields), enter your registered email, and follow the prompts to verify your email and set a new password. You do not need to contact support to do this.

If you registered using Google, Microsoft, or ADDI, you do not have a separate Neuromine password. Sign in with that provider, and reset your password (if needed) in that provider's own account settings — the portal's "Forgot your password?" link applies only to local email/password accounts.

If the verification email does not arrive, check your spam or junk folder and request it again. If you still cannot reset your password, contact data@answerals.org.

---

# Section 2: Account Already Exists

*This is a specific and commonly reported issue where a user cannot sign in but also cannot register a new account. It is caused by an authentication method mismatch: a user originally registered using one method (e.g., Google) but is attempting to sign in or register using a different method (e.g., local Neuromine). This has been confirmed and reproduced.*

Q: When I try to sign in, it says I am not recognized. But when I try to register, it says my account already exists. What is happening?

Context: This occurs when a user registered using one authentication method but is now attempting to sign in or register using a different one. Registering with Google then attempting the local Neuromine sign-in flow allows the verification code email to be sent, but clicking "Create" produces the "already registered" error because the email is already associated with the Google account.

A: Your account already exists, but you are trying to sign in using a different method than the one you originally used to register. The portal supports four sign-in methods: local Neuromine registration, ADDI, Microsoft, and Google. You must always sign in using the same method you used when you first created your account. Try each of the sign-in methods you may have used during registration. If you are unsure which method you registered with, contact data@answerals.org and the team can look up your account details.

---

# Section 3: Changing Account Email or Name

*Users occasionally need to update the email address or name on their account. There is currently no self-service functionality for either of these changes — both must be handled by the support team.*

Q: How do I change the email address on my account?

Context: A user may need to change their account email due to changing institutions, switching to a different professional email, or correcting a typo made during registration. The portal does not offer a self-service option for email changes.

A: Changing the email address associated with your account is not currently available as a self-service option. If you need to change your email address, contact data@answerals.org and the team will assist you.

---

Q: How do I change my name on my account?

Context: A user may need to update the name displayed on their account due to a legal name change, a correction, or an institutional affiliation update. The portal does not offer a self-service option for name changes.

A: Changing the name on your account is not currently available as a self-service option. If you need to update your name, contact data@answerals.org and the team will assist you.

---

# Section 4: Account Deletion

*Users may request account deletion for various reasons. Account deletion is handled by the support team and can be scoped to either the data access request only or the entire account, depending on the user's needs.*

Q: How do I delete my account?

Context: A user may want to delete their account due to leaving their institution, no longer needing data access, or data privacy preferences. Account deletion is not a self-service action and must be processed by the Neuromine support team.

A: To delete your account, contact data@answerals.org with your request. When you reach out, let the team know whether you would like to delete only your current data access request while keeping your account, or whether you would like to delete your entire account and all associated records. The team will clarify the scope with you and process it accordingly.

---

# Section 5: Download Tool Login Conflicts

*The Neuromine Data Portal and the download tool use the same authentication system. Users can be logged into both at the same time without conflict. Login issues with the download tool are not caused by an active portal session.*

Q: I'm having trouble logging into the download tool because I'm already logged into Neuromine. What should I do?

Context: Users sometimes believe that being logged into the Neuromine Data Portal prevents them from logging into the download tool. In fact, both applications use the same authentication system and being logged into one does not interfere with the other.

A: Being logged into the Neuromine Data Portal does not prevent you from logging into the download tool. Both applications use the same authentication system and you can be signed into both at the same time. If you are experiencing login issues with the download tool, the cause is unrelated to your portal session. Try logging in again, and if the issue persists, contact data@answerals.org.

---

Q: I logged into the download tool and it is showing me a blank screen. What is wrong?

Context: Users have reported seeing a blank screen after authenticating with the download tool. The download tool is a desktop application, not a browser-based tool. This is not caused by a session conflict with the Neuromine Data Portal.

A: The download tool is a desktop application. If it is showing a blank screen after login:
1. Close the application completely and reopen it.
2. Check that you are running the latest version and update if needed.
3. Uninstall and reinstall the tool from the Neuromine Data Portal.
4. Verify your operating system is supported: Windows 10, Mac OS, Ubuntu 20.04 LTS, Debian 10.4, or CentOS Linux 8.
5. If the problem persists, contact data@answerals.org.

---

# Section 6: Credential Renewal and Account Validity

*User login credentials and Data Use Agreement (DUA) validity operate independently. Credentials do not expire, but the DUA has a defined validity period that requires renewal to maintain dataset access.*

Q: Do my login credentials expire? Do I need to renew them?

Context: Users may be concerned that their portal login will stop working after a period of time or that they need to take action to keep their account active.

A: No, your login credentials for the Neuromine Data Portal do not expire. Once your account is created, you can continue to sign in using the same credentials indefinitely. However, your Data Use Agreement (DUA), which governs your access to datasets, has a separate validity period and does require renewal.

---

Q: Does my Data Use Agreement (DUA) expire? How do I renew it?

Context: The DUA is a separate authorization from the user account itself. While user credentials do not expire, the DUA has a defined validity period and requires renewal to maintain data access.

A: Yes, your Data Use Agreement (DUA) has a validity period of four years from the date it was approved. After four years, you will need to renew your DUA to maintain access to datasets on the portal. For questions about DUA renewal, including timing and the renewal process, contact data@answerals.org.

---

Q: How will I know if my account has been deleted or my access request has been rejected?

Context: Users may be unsure whether their account is still active or whether a data access request has been processed.

A: If your account is deleted or your data access request is rejected, you will be notified via email to the address associated with your account. If you are unsure about your current account or access status, contact data@answerals.org.

---

Q: Who do I contact for questions about my account or credentials?

Context: General support inquiry about account management, data access, DUA status, and credential issues.

A: For all questions about your account, data access, credentials, or Data Use Agreement, contact the support team at data@answerals.org.

---

# General Support Reference

For any account or identity issues not covered in this document, or for issues that cannot be resolved through the steps described above, contact the Neuromine Data Portal support team.

Support Email: data@answerals.org
