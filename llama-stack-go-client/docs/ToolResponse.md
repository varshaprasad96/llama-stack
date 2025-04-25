# ToolResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CallId** | **string** |  | 
**ToolName** | [**ToolCallToolName**](ToolCallToolName.md) |  | 
**Content** | [**InterleavedContent**](InterleavedContent.md) |  | 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewToolResponse

`func NewToolResponse(callId string, toolName ToolCallToolName, content InterleavedContent, ) *ToolResponse`

NewToolResponse instantiates a new ToolResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolResponseWithDefaults

`func NewToolResponseWithDefaults() *ToolResponse`

NewToolResponseWithDefaults instantiates a new ToolResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCallId

`func (o *ToolResponse) GetCallId() string`

GetCallId returns the CallId field if non-nil, zero value otherwise.

### GetCallIdOk

`func (o *ToolResponse) GetCallIdOk() (*string, bool)`

GetCallIdOk returns a tuple with the CallId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCallId

`func (o *ToolResponse) SetCallId(v string)`

SetCallId sets CallId field to given value.


### GetToolName

`func (o *ToolResponse) GetToolName() ToolCallToolName`

GetToolName returns the ToolName field if non-nil, zero value otherwise.

### GetToolNameOk

`func (o *ToolResponse) GetToolNameOk() (*ToolCallToolName, bool)`

GetToolNameOk returns a tuple with the ToolName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolName

`func (o *ToolResponse) SetToolName(v ToolCallToolName)`

SetToolName sets ToolName field to given value.


### GetContent

`func (o *ToolResponse) GetContent() InterleavedContent`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *ToolResponse) GetContentOk() (*InterleavedContent, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *ToolResponse) SetContent(v InterleavedContent)`

SetContent sets Content field to given value.


### GetMetadata

`func (o *ToolResponse) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ToolResponse) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ToolResponse) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ToolResponse) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


