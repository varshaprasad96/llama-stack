# AgentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SamplingParams** | Pointer to [**SamplingParams**](SamplingParams.md) |  | [optional] 
**InputShields** | Pointer to **[]string** |  | [optional] 
**OutputShields** | Pointer to **[]string** |  | [optional] 
**Toolgroups** | Pointer to [**[]AgentTool**](AgentTool.md) |  | [optional] 
**ClientTools** | Pointer to [**[]ToolDef**](ToolDef.md) |  | [optional] 
**ToolChoice** | Pointer to **string** | Whether tool use is required or automatic. This is a hint to the model which may not be followed. It depends on the Instruction Following capabilities of the model. | [optional] 
**ToolPromptFormat** | Pointer to **string** | Prompt format for calling custom / zero shot tools. | [optional] 
**ToolConfig** | Pointer to [**ToolConfig**](ToolConfig.md) |  | [optional] 
**MaxInferIters** | Pointer to **int32** |  | [optional] [default to 10]
**Model** | **string** | The model identifier to use for the agent | 
**Instructions** | **string** | The system instructions for the agent | 
**Name** | Pointer to **string** | Optional name for the agent, used in telemetry and identification | [optional] 
**EnableSessionPersistence** | Pointer to **bool** | Optional flag indicating whether session data has to be persisted | [optional] [default to false]
**ResponseFormat** | Pointer to [**ResponseFormat**](ResponseFormat.md) | Optional response format configuration | [optional] 

## Methods

### NewAgentConfig

`func NewAgentConfig(model string, instructions string, ) *AgentConfig`

NewAgentConfig instantiates a new AgentConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentConfigWithDefaults

`func NewAgentConfigWithDefaults() *AgentConfig`

NewAgentConfigWithDefaults instantiates a new AgentConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSamplingParams

`func (o *AgentConfig) GetSamplingParams() SamplingParams`

GetSamplingParams returns the SamplingParams field if non-nil, zero value otherwise.

### GetSamplingParamsOk

`func (o *AgentConfig) GetSamplingParamsOk() (*SamplingParams, bool)`

GetSamplingParamsOk returns a tuple with the SamplingParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamplingParams

`func (o *AgentConfig) SetSamplingParams(v SamplingParams)`

SetSamplingParams sets SamplingParams field to given value.

### HasSamplingParams

`func (o *AgentConfig) HasSamplingParams() bool`

HasSamplingParams returns a boolean if a field has been set.

### GetInputShields

`func (o *AgentConfig) GetInputShields() []string`

GetInputShields returns the InputShields field if non-nil, zero value otherwise.

### GetInputShieldsOk

`func (o *AgentConfig) GetInputShieldsOk() (*[]string, bool)`

GetInputShieldsOk returns a tuple with the InputShields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputShields

`func (o *AgentConfig) SetInputShields(v []string)`

SetInputShields sets InputShields field to given value.

### HasInputShields

`func (o *AgentConfig) HasInputShields() bool`

HasInputShields returns a boolean if a field has been set.

### GetOutputShields

`func (o *AgentConfig) GetOutputShields() []string`

GetOutputShields returns the OutputShields field if non-nil, zero value otherwise.

### GetOutputShieldsOk

`func (o *AgentConfig) GetOutputShieldsOk() (*[]string, bool)`

GetOutputShieldsOk returns a tuple with the OutputShields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputShields

`func (o *AgentConfig) SetOutputShields(v []string)`

SetOutputShields sets OutputShields field to given value.

### HasOutputShields

`func (o *AgentConfig) HasOutputShields() bool`

HasOutputShields returns a boolean if a field has been set.

### GetToolgroups

`func (o *AgentConfig) GetToolgroups() []AgentTool`

GetToolgroups returns the Toolgroups field if non-nil, zero value otherwise.

### GetToolgroupsOk

`func (o *AgentConfig) GetToolgroupsOk() (*[]AgentTool, bool)`

GetToolgroupsOk returns a tuple with the Toolgroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolgroups

`func (o *AgentConfig) SetToolgroups(v []AgentTool)`

SetToolgroups sets Toolgroups field to given value.

### HasToolgroups

`func (o *AgentConfig) HasToolgroups() bool`

HasToolgroups returns a boolean if a field has been set.

### GetClientTools

`func (o *AgentConfig) GetClientTools() []ToolDef`

GetClientTools returns the ClientTools field if non-nil, zero value otherwise.

### GetClientToolsOk

`func (o *AgentConfig) GetClientToolsOk() (*[]ToolDef, bool)`

GetClientToolsOk returns a tuple with the ClientTools field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientTools

`func (o *AgentConfig) SetClientTools(v []ToolDef)`

SetClientTools sets ClientTools field to given value.

### HasClientTools

`func (o *AgentConfig) HasClientTools() bool`

HasClientTools returns a boolean if a field has been set.

### GetToolChoice

`func (o *AgentConfig) GetToolChoice() string`

GetToolChoice returns the ToolChoice field if non-nil, zero value otherwise.

### GetToolChoiceOk

`func (o *AgentConfig) GetToolChoiceOk() (*string, bool)`

GetToolChoiceOk returns a tuple with the ToolChoice field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolChoice

`func (o *AgentConfig) SetToolChoice(v string)`

SetToolChoice sets ToolChoice field to given value.

### HasToolChoice

`func (o *AgentConfig) HasToolChoice() bool`

HasToolChoice returns a boolean if a field has been set.

### GetToolPromptFormat

`func (o *AgentConfig) GetToolPromptFormat() string`

GetToolPromptFormat returns the ToolPromptFormat field if non-nil, zero value otherwise.

### GetToolPromptFormatOk

`func (o *AgentConfig) GetToolPromptFormatOk() (*string, bool)`

GetToolPromptFormatOk returns a tuple with the ToolPromptFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolPromptFormat

`func (o *AgentConfig) SetToolPromptFormat(v string)`

SetToolPromptFormat sets ToolPromptFormat field to given value.

### HasToolPromptFormat

`func (o *AgentConfig) HasToolPromptFormat() bool`

HasToolPromptFormat returns a boolean if a field has been set.

### GetToolConfig

`func (o *AgentConfig) GetToolConfig() ToolConfig`

GetToolConfig returns the ToolConfig field if non-nil, zero value otherwise.

### GetToolConfigOk

`func (o *AgentConfig) GetToolConfigOk() (*ToolConfig, bool)`

GetToolConfigOk returns a tuple with the ToolConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolConfig

`func (o *AgentConfig) SetToolConfig(v ToolConfig)`

SetToolConfig sets ToolConfig field to given value.

### HasToolConfig

`func (o *AgentConfig) HasToolConfig() bool`

HasToolConfig returns a boolean if a field has been set.

### GetMaxInferIters

`func (o *AgentConfig) GetMaxInferIters() int32`

GetMaxInferIters returns the MaxInferIters field if non-nil, zero value otherwise.

### GetMaxInferItersOk

`func (o *AgentConfig) GetMaxInferItersOk() (*int32, bool)`

GetMaxInferItersOk returns a tuple with the MaxInferIters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxInferIters

`func (o *AgentConfig) SetMaxInferIters(v int32)`

SetMaxInferIters sets MaxInferIters field to given value.

### HasMaxInferIters

`func (o *AgentConfig) HasMaxInferIters() bool`

HasMaxInferIters returns a boolean if a field has been set.

### GetModel

`func (o *AgentConfig) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *AgentConfig) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *AgentConfig) SetModel(v string)`

SetModel sets Model field to given value.


### GetInstructions

`func (o *AgentConfig) GetInstructions() string`

GetInstructions returns the Instructions field if non-nil, zero value otherwise.

### GetInstructionsOk

`func (o *AgentConfig) GetInstructionsOk() (*string, bool)`

GetInstructionsOk returns a tuple with the Instructions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInstructions

`func (o *AgentConfig) SetInstructions(v string)`

SetInstructions sets Instructions field to given value.


### GetName

`func (o *AgentConfig) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AgentConfig) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AgentConfig) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *AgentConfig) HasName() bool`

HasName returns a boolean if a field has been set.

### GetEnableSessionPersistence

`func (o *AgentConfig) GetEnableSessionPersistence() bool`

GetEnableSessionPersistence returns the EnableSessionPersistence field if non-nil, zero value otherwise.

### GetEnableSessionPersistenceOk

`func (o *AgentConfig) GetEnableSessionPersistenceOk() (*bool, bool)`

GetEnableSessionPersistenceOk returns a tuple with the EnableSessionPersistence field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnableSessionPersistence

`func (o *AgentConfig) SetEnableSessionPersistence(v bool)`

SetEnableSessionPersistence sets EnableSessionPersistence field to given value.

### HasEnableSessionPersistence

`func (o *AgentConfig) HasEnableSessionPersistence() bool`

HasEnableSessionPersistence returns a boolean if a field has been set.

### GetResponseFormat

`func (o *AgentConfig) GetResponseFormat() ResponseFormat`

GetResponseFormat returns the ResponseFormat field if non-nil, zero value otherwise.

### GetResponseFormatOk

`func (o *AgentConfig) GetResponseFormatOk() (*ResponseFormat, bool)`

GetResponseFormatOk returns a tuple with the ResponseFormat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseFormat

`func (o *AgentConfig) SetResponseFormat(v ResponseFormat)`

SetResponseFormat sets ResponseFormat field to given value.

### HasResponseFormat

`func (o *AgentConfig) HasResponseFormat() bool`

HasResponseFormat returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


