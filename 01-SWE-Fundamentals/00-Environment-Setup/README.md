# 00: Environment Setup

Before building AI applications, you must know how to manage Python environments and dependencies. This module introduces the foundational tools and practices that will keep your projects organized, reproducible, and conflict-free.

## What You'll Learn

In this section, you'll learn:

- **Why virtual environments matter** - Understanding dependency conflicts and isolation
- **Traditional Python tooling** - Working with `venv` and `pip`
- **Modern Python workflows** - Using `uv`, a fast, modern Python package manager
- **Project configuration** - Understanding `pyproject.toml` and lock files
- **Backward compatibility** - Using `uv pip` with existing projects

## Files in This Section

- **[WorkingWithEnvironments.ipynb](#./WorkingWithEnvironments.ipynb)** - Interactive notebook covering all concepts with examples
- **[example.py](#./example.py)** - Simple Python script demonstrating basic package usage (numpy and pandas)


## Getting Started

1. Open `WorkingWithEnvironments.ipynb` in your Jupyter environment
2. Follow along with the notebook, reading through each section
3. Try running the example commands in your terminal (not in the notebook cells marked as demonstration)
4. Experiment with creating your own virtual environments

## Key Concepts

### Virtual Environments
Virtual environments create isolated Python environments for each project, preventing dependency conflicts between different projects on your machine.

### Traditional Workflow
The standard Python workflow uses `venv` to create environments and `pip` to install packages. While reliable, this approach can be slow for complex projects.

### Modern Workflow with `uv`
`uv` is a fast, Rust-based Python package manager that provides:
- 10-100x faster package installation than `pip`
- Unified toolchain for environment and dependency management
- Modern project configuration with `pyproject.toml`
- Deterministic builds with lock files

### Project Files
- **`pyproject.toml`** - Modern standard for Python project configuration (PEP 621)
- **`uv.lock`** - Lock file ensuring reproducible builds across machines

## Next Steps

After completing this module, you'll be ready to:
- Set up isolated environments for your AI projects
- Manage dependencies efficiently
- Work with modern Python project structures
- Collaborate effectively with reproducible builds

Proceed to the next module when you're comfortable creating and managing Python environments!
