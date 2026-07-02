from pathlib import Path
import w_r

# @w_r
def main() -> int:
    
    file_path = Path(__file__)
    file_name = file_path.name
    folder_dir = file_path.parent
    project_dir = file_path.parents[2]
    
    print(f"file_path: {file_path}")
    print(f"file_name: {file_name}")
    print(f"folder_dir: {folder_dir}")
    print(f"project_dir: {project_dir}")
    return 1


if __name__ == "__main__":
    # def main():
    #   ...
    #   return 1
    """
    raise SystemExit(main())
    echo $?
    1
    """

    """
    main()
    echo $?
    0
    """
    raise SystemExit(main())

    # raise SystemExit(main()) — not just SystemExit(main())
    # Without 'raise', the exception object is created but never thrown — it's a no-op.
    # main() should return 0 (success) or 1 (failure) so CI can read the exit code.
    
    # CI pipelines (Jenkins, GitHub Actions) read the exit code to decide pass/fail.
    # If your script just calls main() without SystemExit,
    # an exception inside main() might still exit with code 1 
    # — but a clean return always exits 0, even if tests failed.