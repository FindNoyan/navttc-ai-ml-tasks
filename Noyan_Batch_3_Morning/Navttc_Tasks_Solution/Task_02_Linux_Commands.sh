#!/bin/bash
# Task 02 — Linux Commands Demo
# Source: Annexure-I, AI_NAVTTC_Outline_Tasks.pdf
# This script DEMONSTRATES common Linux commands with safe examples.
# Safe commands run for real. DANGEROUS commands (shutdown, restart, rm,
# kill, sudo) appear ONLY as commented-out lines / echo text — never executed.
# Do NOT run this script with sudo. Syntax-check only: bash -n Task_02_Linux_Commands.sh

# ---------------------------------------------------------------------------
# Safety note (read this first):
# This file is for LEARNING. It shows what each command does.
# Commands that can delete data, stop the computer, or kill processes
# are shown as comments starting with '# DANGEROUS — DO NOT RUN:'
# so that nothing harmful happens if you run this script.
# ---------------------------------------------------------------------------

echo "=== Task 02: Linux Commands Demo ==="
echo ""

# --- pwd: print working directory (shows where you are right now) ---
echo "--- pwd: show current directory ---"
pwd
echo ""

# --- cd: change directory ---
# We move into /tmp (a safe temporary folder) and then back.
echo "--- cd: change directory ---"
echo "Moving into /tmp and back:"
cd /tmp
pwd
cd -
echo ""

# --- ls: list files in a directory ---
echo "--- ls: list files ---"
ls
echo "--- ls -l: long format (permissions, size, date) ---"
ls -l | head -n 5
echo ""

# --- mkdir: make a new directory ---
# We create a safe demo folder inside /tmp.
echo "--- mkdir: make a new directory ---"
mkdir -p /tmp/navttc_demo
echo "Created /tmp/navttc_demo"
ls -d /tmp/navttc_demo
echo ""

# --- touch: create an empty file ---
echo "--- touch: create an empty file ---"
touch /tmp/navttc_demo/notes.txt
ls -l /tmp/navttc_demo/
echo ""

# --- cat: show the whole contents of a file ---
echo "--- cat: show file contents ---"
echo "Hello, Linux!" > /tmp/navttc_demo/notes.txt
cat /tmp/navttc_demo/notes.txt
echo ""

# --- cp: copy a file ---
echo "--- cp: copy a file ---"
cp /tmp/navttc_demo/notes.txt /tmp/navttc_demo/notes_copy.txt
ls /tmp/navttc_demo/
echo ""

# --- mv: move / rename a file ---
echo "--- mv: rename a file ---"
mv /tmp/navttc_demo/notes_copy.txt /tmp/navttc_demo/notes_renamed.txt
ls /tmp/navttc_demo/
echo ""

# --- file: tell what type a file is ---
echo "--- file: show file type ---"
file /tmp/navttc_demo/notes.txt
echo ""

# --- head: show the first lines of a file ---
echo "--- head: show first lines ---"
head -n 5 /tmp/navttc_demo/notes.txt
echo ""

# --- more / less: page through a file (interactive viewers) ---
# These open a viewer you scroll with Space and quit with 'q'.
# They are shown here as echo text only, because they wait for key presses.
echo "--- more / less: page through a file (interactive) ---"
echo "more /tmp/navttc_demo/notes.txt   # press Space to scroll, q to quit"
echo "less /tmp/navttc_demo/notes.txt   # same, but you can scroll up too"
echo ""

# --- redirection: send command output into a file with > or >> ---
echo "--- redirection: > overwrites, >> appends ---"
echo "Line one" > /tmp/navttc_demo/redirect.txt
echo "Line two" >> /tmp/navttc_demo/redirect.txt
cat /tmp/navttc_demo/redirect.txt
echo ""

# --- alias: a short nickname for a longer command ---
echo "--- alias: nickname for a command ---"
alias ll='ls -l'
echo "Created alias: ll = ls -l"
alias ll
echo ""

# --- chmod: change file permissions ---
# Here we make notes.txt readable/writable only by the owner (safe demo).
echo "--- chmod: change permissions ---"
chmod 600 /tmp/navttc_demo/notes.txt
ls -l /tmp/navttc_demo/notes.txt
echo ""

# --- ps: list running processes ---
echo "--- ps: list running processes ---"
ps aux | head -n 5
echo ""

# --- nano: a simple terminal text editor ---
# nano opens an editor you type in and exit with Ctrl+X.
# Shown as echo text only, because it waits for you to type.
echo "--- nano: simple text editor (interactive) ---"
echo "nano /tmp/navttc_demo/notes.txt   # edit, then Ctrl+X to exit"
echo ""

# --- bash / sh: shells that run commands and scripts ---
echo "--- bash / sh: shells ---"
echo "bash --version | head -n 1"
bash --version | head -n 1
echo "sh is a simpler shell; bash is the usual default shell."
echo ""

# --- man: show the manual page for a command ---
# man opens an interactive viewer, so we show it as echo text only.
echo "--- man: manual page for a command (interactive) ---"
echo "man ls   # shows help for ls; press q to quit"
echo ""

# --- rmdir: remove an EMPTY directory ---
echo "--- rmdir: remove an empty directory ---"
mkdir -p /tmp/navttc_demo/empty_folder
rmdir /tmp/navttc_demo/empty_folder
echo "Removed empty_folder with rmdir."
echo ""

# --- rm: delete files (DANGEROUS: deleted files do not go to a recycle bin) ---
echo "--- rm: delete files — DANGEROUS, shown as comments only ---"
echo "rm removes files permanently. We do NOT run it on real files here."
# DANGEROUS — DO NOT RUN: rm /tmp/navttc_demo/notes.txt
# DANGEROUS — DO NOT RUN: rm -rf /tmp/navttc_demo
echo ""

# --- kill: stop a running process by its ID (DANGEROUS if wrong ID) ---
echo "--- kill: stop a process — DANGEROUS, shown as comments only ---"
echo "kill needs a process ID (PID). Killing the wrong PID can stop important programs."
# DANGEROUS — DO NOT RUN: kill 1234
# DANGEROUS — DO NOT RUN: kill -9 1234
echo ""

# --- sudo: run a command as administrator / root (DANGEROUS) ---
echo "--- sudo: run as administrator — DANGEROUS, shown as comments only ---"
echo "sudo gives full power. Only use it when you understand the command."
# DANGEROUS — DO NOT RUN: sudo apt update
# DANGEROUS — DO NOT RUN: sudo rm -rf /
echo ""

# --- dpkg: install / list Debian packages (needs sudo, so shown as text) ---
echo "--- dpkg: Debian package tool ---"
echo "dpkg -l | head   # list installed packages"
echo "On Ubuntu/Debian, installing needs sudo, so we do not run it here:"
# DANGEROUS — DO NOT RUN (needs admin): sudo dpkg -i some-package.deb
echo ""

# --- shutdown / restart: turn off or reboot the computer (DANGEROUS) ---
echo "--- shutdown / restart — DANGEROUS, shown as comments only ---"
echo "These would turn off or reboot your computer. Never run them in a demo."
# DANGEROUS — DO NOT RUN: shutdown now
# DANGEROUS — DO NOT RUN: shutdown -h now
# DANGEROUS — DO NOT RUN: restart
# DANGEROUS — DO NOT RUN: reboot
echo ""

# --- Cleanup of our own safe demo folder ---
# We use rm here ONLY on the demo folder we created, inside /tmp.
# In the submitted script the dangerous rm lines above stay commented out.
# (This cleanup line is kept commented too, so the script never deletes anything.)
# rm -rf /tmp/navttc_demo

echo "=== Demo finished ==="
echo "Safe commands ran for real. Dangerous commands were shown as comments only."

# Sample output:
# === Task 02: Linux Commands Demo ===
# --- pwd: show current directory ---
# /home/hatch
# --- cd: change directory ---
# Moving into /tmp and back:
# /tmp
# /home/hatch
# --- ls: list files ---
# (listing of files in the current directory)
# --- mkdir: make a new directory ---
# Created /tmp/navttc_demo
# /tmp/navttc_demo
# --- touch: create an empty file ---
# (listing shows notes.txt)
# --- cat: show file contents ---
# Hello, Linux!
# --- cp: copy a file ---
# notes.txt  notes_copy.txt
# --- mv: rename a file ---
# notes.txt  notes_renamed.txt
# --- file: show file type ---
# /tmp/navttc_demo/notes.txt: ASCII text
# --- head: show first lines ---
# Hello, Linux!
# --- more / less: page through a file (interactive) ---
# more /tmp/navttc_demo/notes.txt   # press Space to scroll, q to quit
# less /tmp/navttc_demo/notes.txt   # same, but you can scroll up too
# --- redirection: > overwrites, >> appends ---
# Line one
# Line two
# --- alias: nickname for a command ---
# Created alias: ll = ls -l
# alias ll='ls -l'
# --- chmod: change permissions ---
# -rw------- ... notes.txt
# --- ps: list running processes ---
# (first 5 lines of the process list)
# --- nano: simple text editor (interactive) ---
# nano /tmp/navttc_demo/notes.txt   # edit, then Ctrl+X to exit
# --- bash / sh: shells ---
# bash --version | head -n 1
# GNU bash, version 5.x ...
# sh is a simpler shell; bash is the usual default shell.
# --- man: manual page for a command (interactive) ---
# man ls   # shows help for ls; press q to quit
# --- rmdir: remove an empty directory ---
# Removed empty_folder with rmdir.
# --- rm: delete files — DANGEROUS, shown as comments only ---
# rm removes files permanently. We do NOT run it on real files here.
# --- kill: stop a process — DANGEROUS, shown as comments only ---
# kill needs a process ID (PID). Killing the wrong PID can stop important programs.
# --- sudo: run as administrator — DANGEROUS, shown as comments only ---
# sudo gives full power. Only use it when you understand the command.
# --- dpkg: Debian package tool ---
# dpkg -l | head   # list installed packages
# On Ubuntu/Debian, installing needs sudo, so we do not run it here:
# --- shutdown / restart — DANGEROUS, shown as comments only ---
# These would turn off or reboot your computer. Never run them in a demo.
# === Demo finished ===
# Safe commands ran for real. Dangerous commands were shown as comments only.
