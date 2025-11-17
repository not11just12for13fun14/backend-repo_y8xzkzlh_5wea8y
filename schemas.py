"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# Example schemas (kept for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in rupees")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Pappa ji ka Dosa app schemas

class MenuItem(BaseModel):
    """Menu items for the restaurant
    Collection name: "menuitem" -> typically used as "menuitem" collection
    """
    name: str = Field(..., description="Dish name")
    description: Optional[str] = Field(None, description="Short description")
    price: float = Field(..., ge=0, description="Price in INR")
    category: str = Field(..., description="Category e.g., Dosa, Bihari, South Indian, Drinks")
    is_spicy: bool = Field(False, description="Spice indicator")
    is_veg: bool = Field(True, description="Vegetarian indicator")
    tags: Optional[List[str]] = Field(default=None, description="Additional tags like 'bestseller', 'new'")
    image_url: Optional[str] = Field(None, description="Optional image URL")

class Reservation(BaseModel):
    """Reservations made by customers
    Collection name: "reservation"
    """
    name: str = Field(..., description="Customer name")
    email: Optional[EmailStr] = Field(None, description="Email address")
    phone: str = Field(..., description="Contact number")
    date: str = Field(..., description="Date (YYYY-MM-DD)")
    time: str = Field(..., description="Time (HH:MM)")
    guests: int = Field(..., ge=1, le=20, description="Number of guests")
    special_request: Optional[str] = Field(None, description="Any special request")

class ContactMessage(BaseModel):
    """General contact messages
    Collection name: "contactmessage"
    """
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    message: str
