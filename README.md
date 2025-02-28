# Group Tasks Repository

This repository is designed for submitting group programming tasks for the Advanced Python course. Please follow these instructions carefully to submit your group's work.

## Repository Structure

Each group has their own designated folder within this repository. Only group leaders have write access to their group's folder as specified in the CODEOWNERS file.

## How to Submit Group Tasks

### 1. Initial Setup (All Group Members)
```bash
# Clone the repository
git clone <repository-url>
cd Group-Tasks

# Create and switch to a new branch for your feature
git checkout -b task/group-<number>/feature-name
```

### 2. Adding Your Work (All Group Members)
- Place your files ONLY in your group's designated folder
- Make sure to include:
  - Source code files (.py)
  - Requirements.txt (if needed)
  - Documentation explaining your solution
  - Your name and contribution description

### 3. Collaboration Process
1. Each group member can:
   - Create new branches for their features
   - Commit and push their code
   - Create pull requests to the group's task branch
2. Group leader is responsible for:
   - Reviewing pull requests from team members
   - Approving or requesting changes
   - Ensuring code quality and consistency
   - Managing the final submission

### 4. Committing and Pushing (All Group Members)
```bash
# Add your changes
git add your-group-folder/*

# Commit with a descriptive message
git commit -m "Add feature X for Group Task Y"

# Push to your feature branch
git push origin task/group-<number>/feature-name
```

### 5. Creating Pull Requests
1. Group members:
   - Create pull requests to the group's task branch
   - Write clear descriptions of their contributions
   - Address review comments from the group leader
2. Group leader:
   - Reviews and manages pull requests
   - Ensures all contributions are properly integrated
   - Creates the final pull request to main branch

## Important Notes

- ⚠️ Never commit directly to the main branch
- ⚠️ Only modify files within your group's folder
- ✅ Create feature branches for your contributions
- ✅ Wait for group leader's review before merging
- ✅ Group leader approves final submission to main
- ❌ Pull requests modifying other groups' folders will be rejected

## Best Practices

1. Coordinate with your group members effectively
2. Use consistent coding style across the group
3. Review each other's code before submission
4. Test thoroughly as a group
5. Document group decisions and implementation choices

## Need Help?

If you encounter any issues with the group submission process, please contact the course instructor or teaching assistants.