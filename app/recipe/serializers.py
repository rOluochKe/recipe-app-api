"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import (
    Recipe,
)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'price', 'link',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a recipe."""
        recipe = Recipe.objects.create(**validated_data)

        return recipe

    def update(self, instance, validated_data):
        """Update recipe."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
