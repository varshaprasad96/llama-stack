# ContentDelta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | [default to "text"]
**Text** | **string** |  | 
**Image** | **string** |  | 
**ToolCall** | [**ToolCallDeltaToolCall**](ToolCallDeltaToolCall.md) |  | 
**ParseStatus** | **string** |  | 

## Methods

### NewContentDelta

`func NewContentDelta(type_ string, text string, image string, toolCall ToolCallDeltaToolCall, parseStatus string, ) *ContentDelta`

NewContentDelta instantiates a new ContentDelta object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentDeltaWithDefaults

`func NewContentDeltaWithDefaults() *ContentDelta`

NewContentDeltaWithDefaults instantiates a new ContentDelta object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *ContentDelta) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ContentDelta) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ContentDelta) SetType(v string)`

SetType sets Type field to given value.


### GetText

`func (o *ContentDelta) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *ContentDelta) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *ContentDelta) SetText(v string)`

SetText sets Text field to given value.


### GetImage

`func (o *ContentDelta) GetImage() string`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *ContentDelta) GetImageOk() (*string, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *ContentDelta) SetImage(v string)`

SetImage sets Image field to given value.


### GetToolCall

`func (o *ContentDelta) GetToolCall() ToolCallDeltaToolCall`

GetToolCall returns the ToolCall field if non-nil, zero value otherwise.

### GetToolCallOk

`func (o *ContentDelta) GetToolCallOk() (*ToolCallDeltaToolCall, bool)`

GetToolCallOk returns a tuple with the ToolCall field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolCall

`func (o *ContentDelta) SetToolCall(v ToolCallDeltaToolCall)`

SetToolCall sets ToolCall field to given value.


### GetParseStatus

`func (o *ContentDelta) GetParseStatus() string`

GetParseStatus returns the ParseStatus field if non-nil, zero value otherwise.

### GetParseStatusOk

`func (o *ContentDelta) GetParseStatusOk() (*string, bool)`

GetParseStatusOk returns a tuple with the ParseStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParseStatus

`func (o *ContentDelta) SetParseStatus(v string)`

SetParseStatus sets ParseStatus field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


