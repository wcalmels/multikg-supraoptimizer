"""
Tests for MultiKG SupraOptimizer
"""

import pytest
from multikg_supraoptimizer import MultiKGSupraOptimizer


@pytest.fixture
def system():
    """Create system instance for tests"""
    return MultiKGSupraOptimizer()


def test_initialization(system):
    """Test system initialization"""
    assert system.version == "3.0.0"
    assert system.status == "Production Ready"


def test_process(system):
    """Test process function"""
    result = system.process({"test": "input"})
    
    assert result["status"] == "success"
    assert result["project"] == "MultiKG SupraOptimizer"
    assert result["version"] == "3.0.0"


def test_info(system):
    """Test get_info function"""
    info = system.get_info()
    
    assert info["name"] == "MultiKG SupraOptimizer"
    assert info["version"] == "3.0.0"
    assert info["type"] == "ml"


@pytest.mark.asyncio
async def test_async_process(system):
    """Test async process"""
    result = await system.process_async({"test": "async"})
    assert result["status"] == "success"
