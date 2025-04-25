# AgentTool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** |  | 
**Args** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewAgentTool

`func NewAgentTool(name string, args map[string]AppendRowsRequestRowsInnerValue, ) *AgentTool`

NewAgentTool instantiates a new AgentTool object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentToolWithDefaults

`func NewAgentToolWithDefaults() *AgentTool`

NewAgentToolWithDefaults instantiates a new AgentTool object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *AgentTool) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AgentTool) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AgentTool) SetName(v string)`

SetName sets Name field to given value.


### GetArgs

`func (o *AgentTool) GetArgs() map[string]AppendRowsRequestRowsInnerValue`

GetArgs returns the Args field if non-nil, zero value otherwise.

### GetArgsOk

`func (o *AgentTool) GetArgsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetArgsOk returns a tuple with the Args field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgs

`func (o *AgentTool) SetArgs(v map[string]AppendRowsRequestRowsInnerValue)`

SetArgs sets Args field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


