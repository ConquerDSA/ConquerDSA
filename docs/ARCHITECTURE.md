# 🏗️ ConquerDSA Architecture

> This document describes the technical architecture, design principles, and system flow of ConquerDSA.

---

# Vision

ConquerDSA is an intelligent developer companion that automates coding portfolio management while providing deep analytics, personalized AI guidance, and interview preparation.

The project is built around a single philosophy:

> Collect data once.
> Use it everywhere.

The synchronization layer fetches coding activity from supported platforms only once. Every other module (Dashboard, AI Coach, README Generator, GitHub Automation) consumes the same analytics.

This avoids duplicated computation and keeps every component consistent.

---

# Product Overview

ConquerDSA consists of four major systems.

```

                 ┌──────────────────────┐
                 │      CLI Tool        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Analytics Engine   │
                 └──────────┬───────────┘
                            │
          ┌─────────────────┼──────────────────┐
          ▼                 ▼                  ▼
  README Generator    Web Portal         GitHub Automation
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
      Analytics Dashboard           AI Coach

```

Every component depends on the Analytics Engine.

No component communicates directly with coding platforms except the Synchronization Engine.

---

# High-Level System Architecture

```

                    Coding Platforms

        LeetCode • Codeforces • CodeChef • AtCoder
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Synchronization      │
                 │ Engine              │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Local Data Store    │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Analytics Engine    │
                 └───────┬───────┬─────┘
                         │       │
                         │       │
             ┌───────────┘       └────────────┐
             ▼                                ▼
      README Generator                  Web Portal
             │                                │
             ▼                                │
     GitHub Repository                        │
                                              │
                     ┌────────────────────────┴──────────────────────┐
                     ▼                                               ▼
             Analytics Dashboard                             AI Coach
                                                             │
                                ┌────────────────────────────┼──────────────────────────┐
                                ▼                            ▼                          ▼
                      Weakness Analyzer             Personalized Roadmap        Interview Assistant

```

---

# Core Modules

## CLI

Responsible for user interaction.

Example commands

```

conquerdsa init
conquerdsa sync
conquerdsa doctor
conquerdsa status
conquerdsa dashboard

```

The CLI never computes analytics.

It only orchestrates workflows.

---

## Synchronization Engine

Responsibilities

- Authenticate users
- Fetch coding activity
- Detect solved problems
- Store local cache
- Keep repositories synchronized

Supported Platforms

- LeetCode (V1)
- Codeforces (V2)
- CodeChef (V2)
- AtCoder (V2)

---

## Local Data Store

Stores normalized coding data.

Purpose

- Avoid repeated API calls
- Improve performance
- Enable offline analytics
- Provide one source of truth

---

## Analytics Engine

The heart of ConquerDSA.

Responsible for computing

- Difficulty distribution
- Topic mastery
- Streaks
- Acceptance rate
- Daily activity
- Contest statistics
- Heatmaps
- Progress trends
- Company readiness
- Weak topic identification

Every intelligent feature depends on this engine.

---

## README Generator

Consumes analytics and produces

- Dynamic README
- Statistics
- Badges
- Topic tables
- Progress reports
- Achievement cards

It never computes analytics.

---

## GitHub Automation

Responsible for

- Repository creation
- README updates
- Folder synchronization
- Commit automation
- GitHub Pages deployment

---

# ConquerDSA Portal

The Portal is the primary user interface.

It consists of two major products.

## Analytics Dashboard

Provides

- Heatmaps
- Progress charts
- Topic mastery
- Difficulty breakdown
- Streak visualization
- Repository statistics
- Coding trends

---

## AI Coach

The AI Coach consumes analytics and transforms them into actionable guidance.

Capabilities

- Weakness Analyzer
- Personalized Study Roadmap
- Daily Recommendations
- Company Preparation
- Interview Readiness
- Topic Recommendations
- AI Chat Assistant

The AI Coach never fetches coding platform data directly.

It only consumes analytics.

---

# Folder Structure

```

src/
└── conquerdsa/
├── cli/
├── analytics/
├── sync/
├── github/
├── readme/
├── ai/
├── dashboard/
├── config/
├── models/
├── utils/
└── main.py

```

---

# Design Principles

## Single Source of Truth

Coding platforms are synchronized once.

Every other module consumes analytics.

---

## Separation of Concerns

Synchronization

↓

Analytics

↓

Consumers

No module should perform another module's responsibility.

---

## Modular Architecture

Every module should be replaceable without affecting the rest of the system.

---

## Developer Experience First

Clear commands

Helpful error messages

Minimal configuration

Excellent documentation

---

# Development Workflow

Every feature follows

```

Design

↓

Implement

↓

Test

↓

Commit

↓

Push

↓

Review

```

---

# Version Roadmap

## Version 1

- LeetCode
- GitHub Automation
- Analytics Engine
- Dynamic README
- Portal
- Analytics Dashboard
- AI Coach

---

## Version 2

- Codeforces
- CodeChef
- AtCoder
- Multi-platform analytics
- Team comparison

---

## Version 3

- Community Features
- Mobile Companion
- Browser Extension
- Interview Tracking
- Learning Communities

---

# Philosophy

ConquerDSA is not a synchronization tool.

Synchronization is only the data collection layer.

Analytics is the intelligence layer.

The Portal is the visualization layer.

The AI Coach is the decision layer.

Together they form an intelligent developer companion.