# Patching Guide

Basic requirements to ensure you have a smooth start:

## Prerequisites

1. **Setting Up the IDE (IntelliJ)**
   - Ensure you have IntelliJ installed and properly configured for Android development. You can find a docs on how to set up IntelliJ for Android development [here](./intellij.md).

2. **Setting Up a Gradle Project**
   - Familiarize yourself with Gradle, as it is essential for building and managing dependencies in your project.

3. **Basic Git Commands**
   - Understand fundamental Git commands for version control. This will help you manage your contributions effectively.

4. **Understanding APK Structure**
   - Gain knowledge of how Android applications are compiled and structured within an APK file.

## Environment Setup

To begin contributing, you need a working environment that includes a testing device. Instead of using a physical phone for testing, consider setting up a rooted copy of Android inside a Virtual Device (AVD) instance. I suggest an AVD with a rooted copy of Android 13, because can be easily rooted and has a high compatibility with the majority of applications you will be working with, and it supports easy debugging by using a Proxy. You can find a guide on setting up a Proxy [here](./proxy.md). While this setup may take some effort, it will provide you with an ideal development environment. You can find a guide on setting up an AVD [here](./avd.md).

## Types of Patches

There are two primary types of patches you can create:

### 1. Resource Patches
Resource patches are the easier type of modifications, which involve editing the APK resources to make changes at compile time. To create a resource patch:

- Inspect the application using a Layout Inspector, which will help you identify the resources you want to modify (e.g., layouts, strings, colors). You can find a guide on how to use the Layout Inspector [here](./layout-inspector.md).
- Edit the XML files with the context provided by the ReVanced Patcher.

<!-- TODO: Add an example of a Resource Patch. -->

### 2. Bytecode Patches
Bytecode patches involve heavier modifications, as they utilize the ReVanced framework to edit the Smali code within the decompiled sources of the APK. Creating bytecode patches requires specific knowledge, including:

1. How to use **apktool**. You can find a guide on how to use apktool [here](./apktool.md).
2. How to use **jadx**. You can find a guide on how to use jadx [here](./jadx.md).
3. Basic skills in reading and writing Smali code. You can find a sort of cheatsheet for Smali [here](./smali.md).
4. Familiarity with common patterns used in reverse engineering. This can't be taught by a guide, it's something you will learn by doing. I'll try to provide as much information as possible in the documentation, but the best way to learn this is by experience.

#### Process for Creating a Bytecode Patch

To create a bytecode patch, follow these steps:

1. Use a Layout Inspector to gather clues on which methods to modify. This helps you understand the app's structure and identify the correct method to patch. Knowing that the app uses a specific resource (e.g., a string or a layout id) can help you identify the method that uses it.
2. Decompile the APK using appropriate tools.
3. Identify the correct method to edit. This is the trickiest part, as you need to understand the app's structure and how the methods interact with each other. You can use jadx to help you navigate the decompiled code and find the method you want to modify.
4. Edit the Smali code by hand to apply a Logger method. This is done by adding a hook to a method in the integration module. You can find a guide on how to apply a Logger method [here](./logger.md).
5. Now that you have the correct method identified, you can start writing the Fingerprints for the patch. You can find a guide on how to write Fingerprints [here](./fingerprints.md).
6. Test the patch on your AVD to ensure it works as expected. You can find a guide on how to test a patch [here](./testing.md).

<!-- TODO: Add an example of a Bytecode Patch. -->

You will find numerous commits in the repository that will help you understand this process better.