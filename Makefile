.PHONY: build shell check inspect qc python down clean \
        vep-pull vep-check vep-cache vep-test-input vep-smoke

build:
	docker compose build

shell:
	docker compose run --rm mva bash

check:
	docker compose run --rm mva bash /workspace/scripts/00_check_environment.sh

inspect:
	docker compose run --rm mva bash /workspace/scripts/01_inspect_vcf.sh

qc:
	docker compose run --rm mva bash /workspace/scripts/02_vcf_qc.sh

python:
	docker compose run --rm mva python3 /workspace/pipeline/main.py

vep-pull:
	docker compose pull vep

vep-check:
	docker compose run --rm vep vep --help | head -20

vep-cache:
	docker compose run --rm vep \
		INSTALL.pl \
		-a cf \
		-s homo_sapiens \
		-y GRCh38 \
		--CACHE_VERSION 116 \
		--CACHEDIR /vep_data

vep-test-input:
	docker compose run --rm mva \
		bash /workspace/scripts/03_prepare_vep_test.sh

vep-smoke:
	docker compose run --rm vep \
		vep \
		--input_file /results/private/vep_test.vcf.gz \
		--output_file /results/annotated/vep_test.annotated.vcf \
		--cache \
		--offline \
		--dir_cache /vep_data \
		--species homo_sapiens \
		--assembly GRCh38 \
		--format vcf \
		--vcf \
		--force_overwrite \
		--symbol \
		--canonical \
		--mane \
		--biotype \
		--variant_class \
		--numbers \
		--pick_allele_gene \
		--sift b \
		--polyphen b \
		--af \
		--af_1kg \
		--af_gnomade \
		--af_gnomadg \
		--max_af \
		--clin_sig \
		--fork 8 \
		--no_stats

down:
	docker compose down

clean:
	rm -rf results/qc/*
	rm -rf results/annotated/*
	rm -rf results/ranked/*
	rm -rf results/private/*

bub1b:
	docker compose run --rm mva bash /workspace/scripts/04_extract_bub1b.sh

bub1b-phase:
	docker compose run --rm mva bash /workspace/scripts/05_bub1b_phase.sh
