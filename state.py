from abc import ABC, abstractmethod


# State Interface
class GitRepoState(ABC):
    @abstractmethod
    def stage_changes(self, git_repo):
        pass

    @abstractmethod
    def commit_changes(self, git_repo):
        pass

    @abstractmethod
    def create_branch(self, git_repo, branch_name):
        pass

    @abstractmethod
    def merge_branch(self, git_repo, branch_name):
        pass

    @abstractmethod
    def push_changes(self, git_repo):
        pass

    @abstractmethod
    def pull_changes(self, git_repo):
        pass


# Concrete States
class UnmodifiedState(GitRepoState):
    def stage_changes(self, git_repo):
        print("Staging changes -> Switching to Staged state")
        git_repo.set_state(StagedState())

    def commit_changes(self, git_repo):
        print("No changes to commit")

    def create_branch(self, git_repo, branch_name):
        print(f"Creating branch '{branch_name}'")
        git_repo.branches.append(branch_name)

    def merge_branch(self, git_repo, branch_name):
        if branch_name in git_repo.branches:
            print(f"Merging branch '{branch_name}'")
        else:
            print(f"Branch '{branch_name}' not found")

    def push_changes(self, git_repo):
        print("Pushing changes to remote repository")

    def pull_changes(self, git_repo):
        print("Pulling changes from remote repository")


class ModifiedState(GitRepoState):
    def stage_changes(self, git_repo):
        print("Staging changes -> Switching to Staged state")
        git_repo.set_state(StagedState())

    def commit_changes(self, git_repo):
        print("Changes not staged for commit")

    def create_branch(self, git_repo, branch_name):
        print("Cannot create branch, changes not committed")

    def merge_branch(self, git_repo, branch_name):
        print("Cannot merge branch, changes not committed")

    def push_changes(self, git_repo):
        print("Cannot push changes, changes not committed")

    def pull_changes(self, git_repo):
        print("Cannot pull changes, changes not committed")


class StagedState(GitRepoState):
    def stage_changes(self, git_repo):
        print("Changes already staged")

    def commit_changes(self, git_repo):
        print("Committing changes -> Switching to Unmodified state")
        git_repo.set_state(UnmodifiedState())

    def create_branch(self, git_repo, branch_name):
        print("Cannot create branch, changes not committed")

    def merge_branch(self, git_repo, branch_name):
        print("Cannot merge branch, changes not committed")

    def push_changes(self, git_repo):
        print("Cannot push changes, changes not committed")

    def pull_changes(self, git_repo):
        print("Cannot pull changes, changes not committed")


# Context
class GitRepo:
    def __init__(self):
        self.state = UnmodifiedState()
        self.branches = ['main']

    def set_state(self, state):
        self.state = state

    def stage(self):
        self.state.stage_changes(self)

    def commit(self):
        self.state.commit_changes(self)

    def create_branch(self, branch_name):
        self.state.create_branch(self, branch_name)

    def merge_branch(self, branch_name):
        self.state.merge_branch(self, branch_name)

    def push(self):
        self.state.push_changes(self)

    def pull(self):
        self.state.pull_changes(self)


def main():
    repo = GitRepo()

    # Try committing without changes
    repo.commit()

    # Stage changes and commit
    repo.stage()
    repo.commit()

    # Create a new branch
    repo.create_branch("new-feature")

    # Try creating a branch with uncommitted changes
    repo.stage()
    repo.create_branch("another-feature")

    # Merge the new-feature branch
    repo.commit()
    repo.merge_branch("new-feature")

    # Try merging a non-existing branch
    repo.merge_branch("non-existing")

    # Push and pull in unmodified state
    repo.push()
    repo.pull()

    # Try pushing and pulling with staged changes
    repo.stage()
    repo.push()
    repo.pull()

    # Commit changes and push
    repo.commit()
    repo.push()

    # Pull changes
    repo.pull()


if __name__ == "__main__":
    main()
