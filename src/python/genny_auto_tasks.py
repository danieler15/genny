import subprocess

from shrub.config import Configuration
from shrub.command import CommandDefinition

# https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# def main():
#     print("python main function")


# if __name__ == '__main__':
#     main()


# Loop through src/workloads/ files that have been modified (--> def of mod?)
# git diff --name-only origin/master
# git ls-files -m
# git diff --name-only origin/master -- src/workloads/

out = subprocess.check_output(["git", "diff", "--name-only", "origin/master", "--", "../workloads"])
short_filenames = [f.split("workloads/", 1)[1] for f in out.decode().split('\n')[:-1]]
print(short_filenames)

c = Configuration()

name = "my_test_workload"
# task_names.append(name)
# task_specs.append(TaskSpec(name))
t = c.task(name)
t.commands([
	CommandDefinition().function("prepare environment").vars({
	    "test": name
	}),
    CommandDefinition().function("deploy cluster"),
    CommandDefinition().function("run test"),
    CommandDefinition().function("analyze"),
])

print(c.to_json())



# Auto-generate dsi/configurations/test_control/test_control.{{var}}.yml file:

# task_name: {{var}}
# numactl_prefix_for_workload_client: ${infrastructure_provisioning.numactl_prefix}
# run:
#   - id: {{var}}
#     type: genny
#     config_filename: ./genny/etc/genny/workloads/scale{{UPDATE}}/{{var}}.yml

#   - id: benchRun
#     type: mongoshell
#     cmd: cd workloads && ${test_control.numactl_prefix_for_workload_client} ./run_workloads.py -c ../workloads.yml
#     config_filename: workloads.yml  # The name used in previous row
#     output_files:
#       - workloads/workload_timestamps.csv
#     workload_config:
#       tests:
#         default:
#           - cpu_noise

#       target: ${mongodb_setup.meta.hostname}
#       port: ${mongodb_setup.meta.port}
#       sharded: ${mongodb_setup.meta.is_sharded}
#       replica: ${mongodb_setup.meta.is_replset}
#       shell_ssl_options: ${mongodb_setup.meta.shell_ssl_options}

#   - id: fio
#     type: fio
#     cmd: '${test_control.numactl_prefix_for_workload_client} ./fio-test.sh ${mongodb_setup.meta.hostname}'
#     config_filename: fio.ini
#     output_files:
#       - fio.json
#       - fio_results.tgz
#     workload_config: ${test_control.common_fio_config}
#     skip_validate: true

#   - id: iperf
#     type: iperf
#     output_files:
#       - iperf.json
#     cmd: '${test_control.numactl_prefix_for_workload_client} ./iperf-test.sh ${mongodb_setup.meta.hostname}'
#     skip_validate: true

# pre_task:
#   - on_workload_client:
#       # Drop the database before each run
#       exec_mongo_shell:
#         connection_string: "${mongodb_setup.meta.mongodb_url}"
#         script: |
#           db.dropDatabase();
