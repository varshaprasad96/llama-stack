# Turn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TurnId** | **string** |  | 
**SessionId** | **string** |  | 
**InputMessages** | [**[]CreateAgentTurnRequestMessagesInner**](CreateAgentTurnRequestMessagesInner.md) |  | 
**Steps** | [**[]TurnStepsInner**](TurnStepsInner.md) |  | 
**OutputMessage** | [**CompletionMessage**](CompletionMessage.md) |  | 
**OutputAttachments** | Pointer to [**[]Attachment**](Attachment.md) |  | [optional] 
**StartedAt** | **time.Time** |  | 
**CompletedAt** | Pointer to **time.Time** |  | [optional] 

## Methods

### NewTurn

`func NewTurn(turnId string, sessionId string, inputMessages []CreateAgentTurnRequestMessagesInner, steps []TurnStepsInner, outputMessage CompletionMessage, startedAt time.Time, ) *Turn`

NewTurn instantiates a new Turn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTurnWithDefaults

`func NewTurnWithDefaults() *Turn`

NewTurnWithDefaults instantiates a new Turn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTurnId

`func (o *Turn) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *Turn) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *Turn) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetSessionId

`func (o *Turn) GetSessionId() string`

GetSessionId returns the SessionId field if non-nil, zero value otherwise.

### GetSessionIdOk

`func (o *Turn) GetSessionIdOk() (*string, bool)`

GetSessionIdOk returns a tuple with the SessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionId

`func (o *Turn) SetSessionId(v string)`

SetSessionId sets SessionId field to given value.


### GetInputMessages

`func (o *Turn) GetInputMessages() []CreateAgentTurnRequestMessagesInner`

GetInputMessages returns the InputMessages field if non-nil, zero value otherwise.

### GetInputMessagesOk

`func (o *Turn) GetInputMessagesOk() (*[]CreateAgentTurnRequestMessagesInner, bool)`

GetInputMessagesOk returns a tuple with the InputMessages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputMessages

`func (o *Turn) SetInputMessages(v []CreateAgentTurnRequestMessagesInner)`

SetInputMessages sets InputMessages field to given value.


### GetSteps

`func (o *Turn) GetSteps() []TurnStepsInner`

GetSteps returns the Steps field if non-nil, zero value otherwise.

### GetStepsOk

`func (o *Turn) GetStepsOk() (*[]TurnStepsInner, bool)`

GetStepsOk returns a tuple with the Steps field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSteps

`func (o *Turn) SetSteps(v []TurnStepsInner)`

SetSteps sets Steps field to given value.


### GetOutputMessage

`func (o *Turn) GetOutputMessage() CompletionMessage`

GetOutputMessage returns the OutputMessage field if non-nil, zero value otherwise.

### GetOutputMessageOk

`func (o *Turn) GetOutputMessageOk() (*CompletionMessage, bool)`

GetOutputMessageOk returns a tuple with the OutputMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputMessage

`func (o *Turn) SetOutputMessage(v CompletionMessage)`

SetOutputMessage sets OutputMessage field to given value.


### GetOutputAttachments

`func (o *Turn) GetOutputAttachments() []Attachment`

GetOutputAttachments returns the OutputAttachments field if non-nil, zero value otherwise.

### GetOutputAttachmentsOk

`func (o *Turn) GetOutputAttachmentsOk() (*[]Attachment, bool)`

GetOutputAttachmentsOk returns a tuple with the OutputAttachments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutputAttachments

`func (o *Turn) SetOutputAttachments(v []Attachment)`

SetOutputAttachments sets OutputAttachments field to given value.

### HasOutputAttachments

`func (o *Turn) HasOutputAttachments() bool`

HasOutputAttachments returns a boolean if a field has been set.

### GetStartedAt

`func (o *Turn) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *Turn) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *Turn) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.


### GetCompletedAt

`func (o *Turn) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *Turn) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *Turn) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *Turn) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


