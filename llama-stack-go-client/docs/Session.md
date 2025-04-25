# Session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**SessionId** | **string** |  | 
**SessionName** | **string** |  | 
**Turns** | [**[]Turn**](Turn.md) |  | 
**StartedAt** | **time.Time** |  | 

## Methods

### NewSession

`func NewSession(sessionId string, sessionName string, turns []Turn, startedAt time.Time, ) *Session`

NewSession instantiates a new Session object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSessionWithDefaults

`func NewSessionWithDefaults() *Session`

NewSessionWithDefaults instantiates a new Session object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSessionId

`func (o *Session) GetSessionId() string`

GetSessionId returns the SessionId field if non-nil, zero value otherwise.

### GetSessionIdOk

`func (o *Session) GetSessionIdOk() (*string, bool)`

GetSessionIdOk returns a tuple with the SessionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionId

`func (o *Session) SetSessionId(v string)`

SetSessionId sets SessionId field to given value.


### GetSessionName

`func (o *Session) GetSessionName() string`

GetSessionName returns the SessionName field if non-nil, zero value otherwise.

### GetSessionNameOk

`func (o *Session) GetSessionNameOk() (*string, bool)`

GetSessionNameOk returns a tuple with the SessionName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionName

`func (o *Session) SetSessionName(v string)`

SetSessionName sets SessionName field to given value.


### GetTurns

`func (o *Session) GetTurns() []Turn`

GetTurns returns the Turns field if non-nil, zero value otherwise.

### GetTurnsOk

`func (o *Session) GetTurnsOk() (*[]Turn, bool)`

GetTurnsOk returns a tuple with the Turns field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurns

`func (o *Session) SetTurns(v []Turn)`

SetTurns sets Turns field to given value.


### GetStartedAt

`func (o *Session) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *Session) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *Session) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


