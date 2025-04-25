# LogEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Event** | [**Event**](Event.md) |  | 
**TtlSeconds** | **int32** |  | 

## Methods

### NewLogEventRequest

`func NewLogEventRequest(event Event, ttlSeconds int32, ) *LogEventRequest`

NewLogEventRequest instantiates a new LogEventRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLogEventRequestWithDefaults

`func NewLogEventRequestWithDefaults() *LogEventRequest`

NewLogEventRequestWithDefaults instantiates a new LogEventRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEvent

`func (o *LogEventRequest) GetEvent() Event`

GetEvent returns the Event field if non-nil, zero value otherwise.

### GetEventOk

`func (o *LogEventRequest) GetEventOk() (*Event, bool)`

GetEventOk returns a tuple with the Event field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvent

`func (o *LogEventRequest) SetEvent(v Event)`

SetEvent sets Event field to given value.


### GetTtlSeconds

`func (o *LogEventRequest) GetTtlSeconds() int32`

GetTtlSeconds returns the TtlSeconds field if non-nil, zero value otherwise.

### GetTtlSecondsOk

`func (o *LogEventRequest) GetTtlSecondsOk() (*int32, bool)`

GetTtlSecondsOk returns a tuple with the TtlSeconds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTtlSeconds

`func (o *LogEventRequest) SetTtlSeconds(v int32)`

SetTtlSeconds sets TtlSeconds field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


