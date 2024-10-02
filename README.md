# ReVanced Patcher Framework Docs for New Developers

Welcome to my **ReVanced Patcher Framework Documentation**! This repository is designed to provide comprehensive documentation and guidance to help new developers get started with the ReVanced Patcher framework. Whether you're just getting started or looking to dive deeper into patching Android applications, this guide is for you.

## Table of Contents

- [ReVanced Patcher Framework Docs for New Developers](#revanced-patcher-framework-docs-for-new-developers)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Getting Started](#getting-started)
  - [Key Terms](#key-terms)
    - [1. **Patch**](#1-patch)
    - [2. **Patcher**](#2-patcher)
    - [3. **APK (Android Package Kit)**](#3-apk-android-package-kit)
    - [4. **Decompiling**](#4-decompiling)
    - [5. **Smali**](#5-smali)
    - [6. **Integrations**](#6-integrations)
  - [Prerequisites](#prerequisites)

## Overview

The ReVanced Patcher framework is a tool designed to modify Android applications by applying custom patches. It is open-source and allows developers to contribute patches that alter app behavior, remove ads, enable features, or even add custom functionality.

This documentation aims to help new developers understand the core concepts of the patcher, how to contribute patches, and how to navigate the development environment.

## Getting Started

To get started with the ReVanced Patcher framework, you will need to have basic knowledge of Android development, Java and Kotlin.

## Key Terms

Understanding the following key terms is essential for working with the ReVanced Patcher framework:

### 1. **Patch**
A patch is a piece of code that alters the behavior of an Android application. Patches modify the existing behaviour of an app without accessing the original source code. Patches are written in Java or Kotlin and the interact with smali and resources within the APK.

### 2. **Patcher**
The patcher is the tool responsible for applying patches to an APK (Android Package). It takes an APK file, analyzes it, and applies the necessary modifications as defined by the patches. The ReVanced Patcher framework automates this process, ensuring that patches are correctly injected into the APK.

### 3. **APK (Android Package Kit)**
APK is the file format used by the Android operating system for distributing and installing applications. It's essentially a package that contains all the components (code, resources, assets) needed for an Android app. The ReVanced Patcher, and so the patches, can access all the parts of the APK.

### 4. **Decompiling**
Decompiling refers to the process of converting an APK file's bytecode back into the readable format smali. This step is crucial for analyzing the app and determining _where_ to apply patches. In order to understand the decompilation process, it is important to know the structure of an APK file. Here is a simplified diagram of the compilation steps of an Android application:

![](https://www.researchgate.net/publication/339568697/figure/fig1/AS:863773535510528@1582951067405/Compilation-steps-of-an-Android-application.jpg)

### 5. **Smali**
Smali is the human-readable representation of Android's Dalvik bytecode, which is produced when an APK is decompiled. While patches interact with ReVanced Patcher by using Kotlin, a bytecode patch needs to write directly in the smali code, in order to inject modifications at a lower level.

### 6. **Integrations**
ReVanced Integrations are modules that add additional features to the core application. These integrations allow adding arbitrary Java code to the application, which can be used to extend the functionality of the app. Integrations are written in Java and are compiled into the APK along with the rest of the application. Each integration is a standalone module that can be enabled or disabled independently of the patches selected.


## Prerequisites

- Java 17
- Android SDK
- Git
- Gradle

Key components of the patcher include:

- **Patch Scripts**: Kotlin-based scripts that define the modifications to be made.
- **Analyzer**: Disassembles the APK and scan its smali to identify areas for patching.
- **Applier**: Injects the patches into the appropriate parts of the APK.

Check out my [beginner's guide on what is a patch](docs/patch.md) for a detailed tutorial on patch creation and application.