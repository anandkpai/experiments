"""
    Argo Workflows API

    Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. For more information, please see https://argoproj.github.io/argo-workflows/  # noqa: E501

    The version of the OpenAPI document: VERSION
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from argo_workflows.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from argo_workflows.exceptions import ApiAttributeError


def lazy_import():
    from argo_workflows.model.affinity import Affinity
    from argo_workflows.model.container import Container
    from argo_workflows.model.host_alias import HostAlias
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_artifact_location import IoArgoprojWorkflowV1alpha1ArtifactLocation
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_container_set_template import IoArgoprojWorkflowV1alpha1ContainerSetTemplate
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_dag_template import IoArgoprojWorkflowV1alpha1DAGTemplate
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_data import IoArgoprojWorkflowV1alpha1Data
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_executor_config import IoArgoprojWorkflowV1alpha1ExecutorConfig
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_http import IoArgoprojWorkflowV1alpha1HTTP
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_inputs import IoArgoprojWorkflowV1alpha1Inputs
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_memoize import IoArgoprojWorkflowV1alpha1Memoize
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_metadata import IoArgoprojWorkflowV1alpha1Metadata
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_metrics import IoArgoprojWorkflowV1alpha1Metrics
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_outputs import IoArgoprojWorkflowV1alpha1Outputs
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_parallel_steps import IoArgoprojWorkflowV1alpha1ParallelSteps
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_resource_template import IoArgoprojWorkflowV1alpha1ResourceTemplate
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_retry_strategy import IoArgoprojWorkflowV1alpha1RetryStrategy
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_script_template import IoArgoprojWorkflowV1alpha1ScriptTemplate
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_suspend_template import IoArgoprojWorkflowV1alpha1SuspendTemplate
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_synchronization import IoArgoprojWorkflowV1alpha1Synchronization
    from argo_workflows.model.io_argoproj_workflow_v1alpha1_user_container import IoArgoprojWorkflowV1alpha1UserContainer
    from argo_workflows.model.pod_security_context import PodSecurityContext
    from argo_workflows.model.toleration import Toleration
    from argo_workflows.model.volume import Volume
    globals()['Affinity'] = Affinity
    globals()['Container'] = Container
    globals()['HostAlias'] = HostAlias
    globals()['IoArgoprojWorkflowV1alpha1ArtifactLocation'] = IoArgoprojWorkflowV1alpha1ArtifactLocation
    globals()['IoArgoprojWorkflowV1alpha1ContainerSetTemplate'] = IoArgoprojWorkflowV1alpha1ContainerSetTemplate
    globals()['IoArgoprojWorkflowV1alpha1DAGTemplate'] = IoArgoprojWorkflowV1alpha1DAGTemplate
    globals()['IoArgoprojWorkflowV1alpha1Data'] = IoArgoprojWorkflowV1alpha1Data
    globals()['IoArgoprojWorkflowV1alpha1ExecutorConfig'] = IoArgoprojWorkflowV1alpha1ExecutorConfig
    globals()['IoArgoprojWorkflowV1alpha1HTTP'] = IoArgoprojWorkflowV1alpha1HTTP
    globals()['IoArgoprojWorkflowV1alpha1Inputs'] = IoArgoprojWorkflowV1alpha1Inputs
    globals()['IoArgoprojWorkflowV1alpha1Memoize'] = IoArgoprojWorkflowV1alpha1Memoize
    globals()['IoArgoprojWorkflowV1alpha1Metadata'] = IoArgoprojWorkflowV1alpha1Metadata
    globals()['IoArgoprojWorkflowV1alpha1Metrics'] = IoArgoprojWorkflowV1alpha1Metrics
    globals()['IoArgoprojWorkflowV1alpha1Outputs'] = IoArgoprojWorkflowV1alpha1Outputs
    globals()['IoArgoprojWorkflowV1alpha1ParallelSteps'] = IoArgoprojWorkflowV1alpha1ParallelSteps
    globals()['IoArgoprojWorkflowV1alpha1ResourceTemplate'] = IoArgoprojWorkflowV1alpha1ResourceTemplate
    globals()['IoArgoprojWorkflowV1alpha1RetryStrategy'] = IoArgoprojWorkflowV1alpha1RetryStrategy
    globals()['IoArgoprojWorkflowV1alpha1ScriptTemplate'] = IoArgoprojWorkflowV1alpha1ScriptTemplate
    globals()['IoArgoprojWorkflowV1alpha1SuspendTemplate'] = IoArgoprojWorkflowV1alpha1SuspendTemplate
    globals()['IoArgoprojWorkflowV1alpha1Synchronization'] = IoArgoprojWorkflowV1alpha1Synchronization
    globals()['IoArgoprojWorkflowV1alpha1UserContainer'] = IoArgoprojWorkflowV1alpha1UserContainer
    globals()['PodSecurityContext'] = PodSecurityContext
    globals()['Toleration'] = Toleration
    globals()['Volume'] = Volume


class IoArgoprojWorkflowV1alpha1Template(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'active_deadline_seconds': (str,),  # noqa: E501
            'affinity': (Affinity,),  # noqa: E501
            'archive_location': (IoArgoprojWorkflowV1alpha1ArtifactLocation,),  # noqa: E501
            'automount_service_account_token': (bool,),  # noqa: E501
            'container': (Container,),  # noqa: E501
            'container_set': (IoArgoprojWorkflowV1alpha1ContainerSetTemplate,),  # noqa: E501
            'daemon': (bool,),  # noqa: E501
            'dag': (IoArgoprojWorkflowV1alpha1DAGTemplate,),  # noqa: E501
            'data': (IoArgoprojWorkflowV1alpha1Data,),  # noqa: E501
            'executor': (IoArgoprojWorkflowV1alpha1ExecutorConfig,),  # noqa: E501
            'fail_fast': (bool,),  # noqa: E501
            'host_aliases': ([HostAlias],),  # noqa: E501
            'http': (IoArgoprojWorkflowV1alpha1HTTP,),  # noqa: E501
            'init_containers': ([IoArgoprojWorkflowV1alpha1UserContainer],),  # noqa: E501
            'inputs': (IoArgoprojWorkflowV1alpha1Inputs,),  # noqa: E501
            'memoize': (IoArgoprojWorkflowV1alpha1Memoize,),  # noqa: E501
            'metadata': (IoArgoprojWorkflowV1alpha1Metadata,),  # noqa: E501
            'metrics': (IoArgoprojWorkflowV1alpha1Metrics,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'node_selector': ({str: (str,)},),  # noqa: E501
            'outputs': (IoArgoprojWorkflowV1alpha1Outputs,),  # noqa: E501
            'parallelism': (int,),  # noqa: E501
            'plugin': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'pod_spec_patch': (str,),  # noqa: E501
            'priority': (int,),  # noqa: E501
            'priority_class_name': (str,),  # noqa: E501
            'resource': (IoArgoprojWorkflowV1alpha1ResourceTemplate,),  # noqa: E501
            'retry_strategy': (IoArgoprojWorkflowV1alpha1RetryStrategy,),  # noqa: E501
            'scheduler_name': (str,),  # noqa: E501
            'script': (IoArgoprojWorkflowV1alpha1ScriptTemplate,),  # noqa: E501
            'security_context': (PodSecurityContext,),  # noqa: E501
            'service_account_name': (str,),  # noqa: E501
            'sidecars': ([IoArgoprojWorkflowV1alpha1UserContainer],),  # noqa: E501
            'steps': ([IoArgoprojWorkflowV1alpha1ParallelSteps],),  # noqa: E501
            'suspend': (IoArgoprojWorkflowV1alpha1SuspendTemplate,),  # noqa: E501
            'synchronization': (IoArgoprojWorkflowV1alpha1Synchronization,),  # noqa: E501
            'timeout': (str,),  # noqa: E501
            'tolerations': ([Toleration],),  # noqa: E501
            'volumes': ([Volume],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',  # noqa: E501
        'affinity': 'affinity',  # noqa: E501
        'archive_location': 'archiveLocation',  # noqa: E501
        'automount_service_account_token': 'automountServiceAccountToken',  # noqa: E501
        'container': 'container',  # noqa: E501
        'container_set': 'containerSet',  # noqa: E501
        'daemon': 'daemon',  # noqa: E501
        'dag': 'dag',  # noqa: E501
        'data': 'data',  # noqa: E501
        'executor': 'executor',  # noqa: E501
        'fail_fast': 'failFast',  # noqa: E501
        'host_aliases': 'hostAliases',  # noqa: E501
        'http': 'http',  # noqa: E501
        'init_containers': 'initContainers',  # noqa: E501
        'inputs': 'inputs',  # noqa: E501
        'memoize': 'memoize',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'metrics': 'metrics',  # noqa: E501
        'name': 'name',  # noqa: E501
        'node_selector': 'nodeSelector',  # noqa: E501
        'outputs': 'outputs',  # noqa: E501
        'parallelism': 'parallelism',  # noqa: E501
        'plugin': 'plugin',  # noqa: E501
        'pod_spec_patch': 'podSpecPatch',  # noqa: E501
        'priority': 'priority',  # noqa: E501
        'priority_class_name': 'priorityClassName',  # noqa: E501
        'resource': 'resource',  # noqa: E501
        'retry_strategy': 'retryStrategy',  # noqa: E501
        'scheduler_name': 'schedulerName',  # noqa: E501
        'script': 'script',  # noqa: E501
        'security_context': 'securityContext',  # noqa: E501
        'service_account_name': 'serviceAccountName',  # noqa: E501
        'sidecars': 'sidecars',  # noqa: E501
        'steps': 'steps',  # noqa: E501
        'suspend': 'suspend',  # noqa: E501
        'synchronization': 'synchronization',  # noqa: E501
        'timeout': 'timeout',  # noqa: E501
        'tolerations': 'tolerations',  # noqa: E501
        'volumes': 'volumes',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Template - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_deadline_seconds (str): [optional]  # noqa: E501
            affinity (Affinity): [optional]  # noqa: E501
            archive_location (IoArgoprojWorkflowV1alpha1ArtifactLocation): [optional]  # noqa: E501
            automount_service_account_token (bool): AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.. [optional]  # noqa: E501
            container (Container): [optional]  # noqa: E501
            container_set (IoArgoprojWorkflowV1alpha1ContainerSetTemplate): [optional]  # noqa: E501
            daemon (bool): Daemon will allow a workflow to proceed to the next step so long as the container reaches readiness. [optional]  # noqa: E501
            dag (IoArgoprojWorkflowV1alpha1DAGTemplate): [optional]  # noqa: E501
            data (IoArgoprojWorkflowV1alpha1Data): [optional]  # noqa: E501
            executor (IoArgoprojWorkflowV1alpha1ExecutorConfig): [optional]  # noqa: E501
            fail_fast (bool): FailFast, if specified, will fail this template if any of its child pods has failed. This is useful for when this template is expanded with `withItems`, etc.. [optional]  # noqa: E501
            host_aliases ([HostAlias]): HostAliases is an optional list of hosts and IPs that will be injected into the pod spec. [optional]  # noqa: E501
            http (IoArgoprojWorkflowV1alpha1HTTP): [optional]  # noqa: E501
            init_containers ([IoArgoprojWorkflowV1alpha1UserContainer]): InitContainers is a list of containers which run before the main container.. [optional]  # noqa: E501
            inputs (IoArgoprojWorkflowV1alpha1Inputs): [optional]  # noqa: E501
            memoize (IoArgoprojWorkflowV1alpha1Memoize): [optional]  # noqa: E501
            metadata (IoArgoprojWorkflowV1alpha1Metadata): [optional]  # noqa: E501
            metrics (IoArgoprojWorkflowV1alpha1Metrics): [optional]  # noqa: E501
            name (str): Name is the name of the template. [optional]  # noqa: E501
            node_selector ({str: (str,)}): NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level.. [optional]  # noqa: E501
            outputs (IoArgoprojWorkflowV1alpha1Outputs): [optional]  # noqa: E501
            parallelism (int): Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total.. [optional]  # noqa: E501
            plugin (bool, date, datetime, dict, float, int, list, str, none_type): Plugin is an Object with exactly one key. [optional]  # noqa: E501
            pod_spec_patch (str): PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).. [optional]  # noqa: E501
            priority (int): Priority to apply to workflow pods.. [optional]  # noqa: E501
            priority_class_name (str): PriorityClassName to apply to workflow pods.. [optional]  # noqa: E501
            resource (IoArgoprojWorkflowV1alpha1ResourceTemplate): [optional]  # noqa: E501
            retry_strategy (IoArgoprojWorkflowV1alpha1RetryStrategy): [optional]  # noqa: E501
            scheduler_name (str): If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler.. [optional]  # noqa: E501
            script (IoArgoprojWorkflowV1alpha1ScriptTemplate): [optional]  # noqa: E501
            security_context (PodSecurityContext): [optional]  # noqa: E501
            service_account_name (str): ServiceAccountName to apply to workflow pods. [optional]  # noqa: E501
            sidecars ([IoArgoprojWorkflowV1alpha1UserContainer]): Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes. [optional]  # noqa: E501
            steps ([IoArgoprojWorkflowV1alpha1ParallelSteps]): Steps define a series of sequential/parallel workflow steps. [optional]  # noqa: E501
            suspend (IoArgoprojWorkflowV1alpha1SuspendTemplate): [optional]  # noqa: E501
            synchronization (IoArgoprojWorkflowV1alpha1Synchronization): [optional]  # noqa: E501
            timeout (str): Timeout allows to set the total node execution timeout duration counting from the node's start time. This duration also includes time in which the node spends in Pending state. This duration may not be applied to Step or DAG templates.. [optional]  # noqa: E501
            tolerations ([Toleration]): Tolerations to apply to workflow pods.. [optional]  # noqa: E501
            volumes ([Volume]): Volumes is a list of volumes that can be mounted by containers in a template.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """IoArgoprojWorkflowV1alpha1Template - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            active_deadline_seconds (str): [optional]  # noqa: E501
            affinity (Affinity): [optional]  # noqa: E501
            archive_location (IoArgoprojWorkflowV1alpha1ArtifactLocation): [optional]  # noqa: E501
            automount_service_account_token (bool): AutomountServiceAccountToken indicates whether a service account token should be automatically mounted in pods. ServiceAccountName of ExecutorConfig must be specified if this value is false.. [optional]  # noqa: E501
            container (Container): [optional]  # noqa: E501
            container_set (IoArgoprojWorkflowV1alpha1ContainerSetTemplate): [optional]  # noqa: E501
            daemon (bool): Daemon will allow a workflow to proceed to the next step so long as the container reaches readiness. [optional]  # noqa: E501
            dag (IoArgoprojWorkflowV1alpha1DAGTemplate): [optional]  # noqa: E501
            data (IoArgoprojWorkflowV1alpha1Data): [optional]  # noqa: E501
            executor (IoArgoprojWorkflowV1alpha1ExecutorConfig): [optional]  # noqa: E501
            fail_fast (bool): FailFast, if specified, will fail this template if any of its child pods has failed. This is useful for when this template is expanded with `withItems`, etc.. [optional]  # noqa: E501
            host_aliases ([HostAlias]): HostAliases is an optional list of hosts and IPs that will be injected into the pod spec. [optional]  # noqa: E501
            http (IoArgoprojWorkflowV1alpha1HTTP): [optional]  # noqa: E501
            init_containers ([IoArgoprojWorkflowV1alpha1UserContainer]): InitContainers is a list of containers which run before the main container.. [optional]  # noqa: E501
            inputs (IoArgoprojWorkflowV1alpha1Inputs): [optional]  # noqa: E501
            memoize (IoArgoprojWorkflowV1alpha1Memoize): [optional]  # noqa: E501
            metadata (IoArgoprojWorkflowV1alpha1Metadata): [optional]  # noqa: E501
            metrics (IoArgoprojWorkflowV1alpha1Metrics): [optional]  # noqa: E501
            name (str): Name is the name of the template. [optional]  # noqa: E501
            node_selector ({str: (str,)}): NodeSelector is a selector to schedule this step of the workflow to be run on the selected node(s). Overrides the selector set at the workflow level.. [optional]  # noqa: E501
            outputs (IoArgoprojWorkflowV1alpha1Outputs): [optional]  # noqa: E501
            parallelism (int): Parallelism limits the max total parallel pods that can execute at the same time within the boundaries of this template invocation. If additional steps/dag templates are invoked, the pods created by those templates will not be counted towards this total.. [optional]  # noqa: E501
            plugin (bool, date, datetime, dict, float, int, list, str, none_type): Plugin is an Object with exactly one key. [optional]  # noqa: E501
            pod_spec_patch (str): PodSpecPatch holds strategic merge patch to apply against the pod spec. Allows parameterization of container fields which are not strings (e.g. resource limits).. [optional]  # noqa: E501
            priority (int): Priority to apply to workflow pods.. [optional]  # noqa: E501
            priority_class_name (str): PriorityClassName to apply to workflow pods.. [optional]  # noqa: E501
            resource (IoArgoprojWorkflowV1alpha1ResourceTemplate): [optional]  # noqa: E501
            retry_strategy (IoArgoprojWorkflowV1alpha1RetryStrategy): [optional]  # noqa: E501
            scheduler_name (str): If specified, the pod will be dispatched by specified scheduler. Or it will be dispatched by workflow scope scheduler if specified. If neither specified, the pod will be dispatched by default scheduler.. [optional]  # noqa: E501
            script (IoArgoprojWorkflowV1alpha1ScriptTemplate): [optional]  # noqa: E501
            security_context (PodSecurityContext): [optional]  # noqa: E501
            service_account_name (str): ServiceAccountName to apply to workflow pods. [optional]  # noqa: E501
            sidecars ([IoArgoprojWorkflowV1alpha1UserContainer]): Sidecars is a list of containers which run alongside the main container Sidecars are automatically killed when the main container completes. [optional]  # noqa: E501
            steps ([IoArgoprojWorkflowV1alpha1ParallelSteps]): Steps define a series of sequential/parallel workflow steps. [optional]  # noqa: E501
            suspend (IoArgoprojWorkflowV1alpha1SuspendTemplate): [optional]  # noqa: E501
            synchronization (IoArgoprojWorkflowV1alpha1Synchronization): [optional]  # noqa: E501
            timeout (str): Timeout allows to set the total node execution timeout duration counting from the node's start time. This duration also includes time in which the node spends in Pending state. This duration may not be applied to Step or DAG templates.. [optional]  # noqa: E501
            tolerations ([Toleration]): Tolerations to apply to workflow pods.. [optional]  # noqa: E501
            volumes ([Volume]): Volumes is a list of volumes that can be mounted by containers in a template.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
