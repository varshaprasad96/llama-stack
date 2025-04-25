# OpenAIChatCompletionToolCall

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Index** | Pointer to **int32** |  | [optional] 
**Id** | Pointer to **string** |  | [optional] 
**Type** | **string** |  | [default to "function"]
**Function** | Pointer to [**OpenAIChatCompletionToolCallFunction**](OpenAIChatCompletionToolCallFunction.md) |  | [optional] 

## Methods

### NewOpenAIChatCompletionToolCall

`func NewOpenAIChatCompletionToolCall(type_ string, ) *OpenAIChatCompletionToolCall`

NewOpenAIChatCompletionToolCall instantiates a new OpenAIChatCompletionToolCall object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOpenAIChatCompletionToolCallWithDefaults

`func NewOpenAIChatCompletionToolCallWithDefaults() *OpenAIChatCompletionToolCall`

NewOpenAIChatCompletionToolCallWithDefaults instantiates a new OpenAIChatCompletionToolCall object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIndex

`func (o *OpenAIChatCompletionToolCall) GetIndex() int32`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *OpenAIChatCompletionToolCall) GetIndexOk() (*int32, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *OpenAIChatCompletionToolCall) SetIndex(v int32)`

SetIndex sets Index field to given value.

### HasIndex

`func (o *OpenAIChatCompletionToolCall) HasIndex() bool`

HasIndex returns a boolean if a field has been set.

### GetId

`func (o *OpenAIChatCompletionToolCall) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *OpenAIChatCompletionToolCall) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *OpenAIChatCompletionToolCall) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *OpenAIChatCompletionToolCall) HasId() bool`

HasId returns a boolean if a field has been set.

### GetType

`func (o *OpenAIChatCompletionToolCall) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *OpenAIChatCompletionToolCall) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *OpenAIChatCompletionToolCall) SetType(v string)`

SetType sets Type field to given value.


### GetFunction

`func (o *OpenAIChatCompletionToolCall) GetFunction() OpenAIChatCompletionToolCallFunction`

GetFunction returns the Function field if non-nil, zero value otherwise.

### GetFunctionOk

`func (o *OpenAIChatCompletionToolCall) GetFunctionOk() (*OpenAIChatCompletionToolCallFunction, bool)`

GetFunctionOk returns a tuple with the Function field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFunction

`func (o *OpenAIChatCompletionToolCall) SetFunction(v OpenAIChatCompletionToolCallFunction)`

SetFunction sets Function field to given value.

### HasFunction

`func (o *OpenAIChatCompletionToolCall) HasFunction() bool`

HasFunction returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


