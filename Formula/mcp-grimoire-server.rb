class McpGrimoireServer < Formula
  desc "Crystal MCP server that indexes documentation via Ollama embeddings"
  homepage "https://github.com/jbox-web/mcp-grimoire-server"
  version "0.1.0"
  license "MIT"

  on_macos do
    on_arm do
      url "https://github.com/jbox-web/mcp-grimoire-server/releases/download/v#{version}/mcp-grimoire-server-darwin-arm64"
      sha256 "0000000000000000000000000000000000000000000000000000000000000000"
    end
    on_intel do
      url "https://github.com/jbox-web/mcp-grimoire-server/releases/download/v#{version}/mcp-grimoire-server-darwin-x86_64"
      sha256 "0000000000000000000000000000000000000000000000000000000000000000"
    end
  end

  on_linux do
    on_arm do
      url "https://github.com/jbox-web/mcp-grimoire-server/releases/download/v#{version}/mcp-grimoire-server-linux-arm64"
      sha256 "0000000000000000000000000000000000000000000000000000000000000000"
    end
    on_intel do
      url "https://github.com/jbox-web/mcp-grimoire-server/releases/download/v#{version}/mcp-grimoire-server-linux-x86_64"
      sha256 "0000000000000000000000000000000000000000000000000000000000000000"
    end
  end

  def install
    binary = Dir["mcp-grimoire-server-*"].first
    bin.install binary => "mcp-grimoire-server"
  end

  test do
    output = shell_output("#{bin}/mcp-grimoire-server info")
    assert_match version.to_s, output
  end
end
