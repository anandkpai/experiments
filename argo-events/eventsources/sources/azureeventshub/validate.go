/*
Copyright 2018 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package azureeventshub

import (
	"context"
	"fmt"

	"github.com/argoproj/argo-events/common"
	"github.com/argoproj/argo-events/pkg/apis/eventsource/v1alpha1"
)

// ValidateEventSource validates azure events hub event source
func (el *EventListener) ValidateEventSource(ctx context.Context) error {
	return validate(&el.AzureEventsHubEventSource)
}

func validate(eventSource *v1alpha1.AzureEventsHubEventSource) error {
	if eventSource == nil {
		return common.ErrNilEventSource
	}
	if eventSource.FQDN == "" {
		return fmt.Errorf("FQDN is not specified")
	}
	if eventSource.HubName == "" {
		return fmt.Errorf("hub name/path is not specified")
	}
	if eventSource.SharedAccessKey == nil {
		return fmt.Errorf("SharedAccessKey is not specified")
	}
	if eventSource.SharedAccessKeyName == nil {
		return fmt.Errorf("SharedAccessKeyName is not specified")
	}
	return nil
}
