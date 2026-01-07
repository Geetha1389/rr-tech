# Terraform RDS Module Repo

This repository contains a small reusable Terraform module for deploying an AWS RDS instance with optional security group and DB subnet group creation.

## Structure
```
modules/
  rds/          # module code
examples/
  simple/       # simple usage example
```

## Quick start
1. Fill in `examples/simple/main.tf` with your subnet IDs and VPC
2. Run `terraform init && terraform apply` in `examples/simple`

## Tips
- Store credentials in `terraform.tfvars` or use `vault`/`secrets manager` to inject
- For production, enable `multi_az` and configure backups and monitoring

## CI — GitHub Actions
A sample GitHub Actions workflow is included at `.github/workflows/terraform-plan.yml` which runs a `terraform init`, `validate`, and `plan` for the `examples/simple` directory.

To enable the workflow, set the following repository secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

The workflow invokes `scripts/ci-terraform-plan.sh` which performs `terraform init`, `validate`, and `plan -out=tfplan` and prints a short plan summary. Adjust Terraform version or job triggers as needed for your CI policy.
