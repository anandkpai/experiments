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

package webhook

import (
	"context"

	"github.com/argoproj/argo-events/common"
	"github.com/argoproj/argo-events/eventsources/common/webhook"
	"github.com/argoproj/argo-events/pkg/apis/eventsource/v1alpha1"
)

// ValidateEventSource validates webhook event source
func (listener *EventListener) ValidateEventSource(ctx context.Context) error {
	return validate(&listener.Webhook)
}

func validate(webhookEventSource *v1alpha1.WebhookEventSource) error {
	if webhookEventSource == nil {
		return common.ErrNilEventSource
	}
	return webhook.ValidateWebhookContext(&webhookEventSource.WebhookContext)
}
