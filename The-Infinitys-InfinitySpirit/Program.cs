// The Infinity's Infinity Style Static Site Generator
using System.Text.Json;

Console.WriteLine("-------Infinity Style Static Site Generator-------");

InfinityStyle.ReadSettingData();

public struct htmlTemp
{
  private htmlTemp(string head, string foot)
  {
    head = "";
    foot = "";
  }
}

public class SettingData
{
  public Dictionary<string, CustomDate>? customDate { get; set; }

  public string? RepositoryName { get; set; }

  public int? RepositoryYear { get; set; }
}

public class CustomDate
{
  public bool? isAutoSet { get; set; }
  public int? CustomYear { get; set; }
  public int? CustomMonth { get; set; }
}

public static class InfinityStyle
{
    public static SettingData? settingData;
  public static void ReadSettingData()
  {
    // 続きはここを見てやろう。
    // https://learn.microsoft.com/ja-jp/dotnet/standard/serialization/system-text-json/deserialization
    StreamReader settingJsonFile = new StreamReader("./setting/setting.json");
    string settingJsonText = settingJsonFile.ReadToEnd();
    Console.WriteLine("Read setting.json:\n\"\"\"\n" + settingJsonText + "\n\"\"\"");
    settingData = JsonSerializer.Deserialize<SettingData>(
        settingJsonText
    );
    Console.WriteLine("--------------------");
    Console.WriteLine("Read Setting Data");
    Console.WriteLine("--------------------");
    Console.WriteLine("Repository Name: "+settingData?.RepositoryName);
    Console.WriteLine("Repository Year: "+settingData?.RepositoryYear);
    Console.WriteLine("--------------------");
  }
}