# Contributing to Ansy

Thank you for considering contributing to **Ansy**! Your code, bug reports, and improvements are very welcome.

---

## **How to Contribute**

### Fork and Clone

Start by forking the repository and cloning it locally:

```bash
git clone https://github.com/anas-shakeel/ansy.git
cd ansy
```

### Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dev Dependencies

Install the package in editable mode with development tools:

```bash
pip install -r requirements-dev.txt
```

### Create a New Branch

Create a new branch for your changes:

```bash
# Checkout a new branch and make your changes
git checkout -b my-new-feature-branch
# Make your changes...
```

### Run Tests

Format the code using `black` and Run tests locally to make sure everything is working as expected.

```bash
black . # Format code
pytest . # Test code
```

Make sure all tests pass before opening a pull request.

### Documentation Updates

If you're updating **function signatures**, **APIs**, **examples**, or **docstrings** that appear in the documentation, please make sure to update the relevant parts of the `docs/` too.

**Ansy** uses `mkdocs` with the **Material for MkDocs** theme to power its documentation.

To preview the docs locally:

```bash
mkdocs serve
# Visit http://localhost:8000
```

**How docs are deployed?**

Documentation is deployed by **Maintainers** using `mkdocs gh-deploy`, But only after pull requests are **reviewed** and **merged**. Contributors **should not** run `mkdocs gh-deploy` themselves.

### Commit Changes and Submit a Pull Request

1. Commit your changes:

    ```bash
    git commit -m "Add a new feature"
    ```

2. Push to your fork:

    ```bash
    git push origin my-new-feature-branch
    ```

3. Open a pull request on GitHub 🙌

---

## **🐞 Reporting Issues**

Found a bug? Something not working as expected? Or maybe the docs are unclear in a spot? We would love to hear from you!

-   🐞 **Bug Reports** – Found something broken? [Open a bug report](https://github.com/Anas-Shakeel/ansy/issues/new?template=bug_report.md) and tell us what’s going wrong.
-   💡 **Feature Requests** – Have an idea that could make Ansy better? [Suggest a feature](https://github.com/Anas-Shakeel/ansy/issues/new?template=feature_request.md).
-   ❓ **Questions** – Curious about something? Need usage help? [Ask a question](https://github.com/Anas-Shakeel/ansy/issues/new?template=question.md).

Each of these comes with a pre-filled template so you know exactly what info to include. It helps us help you faster!

### Before You Open an Issue

-   **Search existing issues**. your bug might already be reported or even fixed!
-   Check if you're using the **latest version** of Ansy (`pip install --upgrade ansy`).
-   Confirm if the bug is specific to your **OS, terminal, or Python version.**

---

## **Thanks for Helping**

Bug reports and feature requests are one of the best ways to help improve the project. Thank you for making Ansy better for everyone! ♥️
