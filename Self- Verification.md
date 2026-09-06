# Project 1 Self-Verification

## Project
Password Strength Checker

## Internship
DecodeLabs Cybersecurity Internship

## Verification Checklist

| Requirement | Status | Verification |
|---|---|---|
| Check password length | PASS | The program checks whether the password contains at least 8 characters. |
| Check for uppercase letters | PASS | The program uses `isupper()` to check for uppercase letters. |
| Check for numbers | PASS | The program uses `isdigit()` to check for numbers. |
| Check for symbols | PASS | The program checks for punctuation/symbol characters. |
| Classify password strength | PASS | The program classifies passwords as Weak, Medium, or Strong. |
| Use `any()` | PASS | The program uses `any()` for the character checks. |
| Test the program | PASS | The program was tested with different fictional passwords. |

## Test Results

### Test 1
Password: `hello`

Result: **Weak**

### Test 2
Password: `CyberTest123`

Result: **Medium**

### Test 3
Password: `CyberTest123@`

Result: **Strong**

## Final Verification

The Password Strength Checker was tested using different fictional passwords and produced the expected strength levels.

The project is ready for submission.
